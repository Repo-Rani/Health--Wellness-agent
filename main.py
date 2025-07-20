from db_collection.db_config import chat_collection
import chainlit as cl
from typing import cast
from config.config import run_config, model
from agent import get_main_agent
from agents import  Agent, RunConfig
from datetime import datetime
from guardrails.input_guardrail import on_user_message
from guardrails.output_guardrails import validate_agent_output
from lifecycle_hooks.hooks import on_agent_start_handler, on_agent_end_handler

from utils.streaming import get_streamed_reply

@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    cl.user_session.set("config", run_config)

    agent: Agent = get_main_agent()
    cl.user_session.set("agent", agent)

    cl.user_session.set("escalation_agent", agent.handoffs[0](model))
    cl.user_session.set("nutrition_expert_agent", agent.handoffs[1](model))
    cl.user_session.set("injury_support_agent", agent.handoffs[2](model))

    welcome_msg = """👋 Hi! I'm your health coach. Tell me your wellness goals - fitness, nutrition, or mental wellbeing.

Examples:
"Help me lose 10kg"
"Suggest vegetarian meal plans"
"Create a home workout routine"

Where shall we begin?"""

    await cl.Message(content=welcome_msg).send()


@cl.on_message
async def main(message: cl.Message):
    if not await on_user_message(message):
        return

    history = cl.user_session.get("chat_history") or []

    # Initial empty message for streaming
    msg = cl.Message(content="")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config = cast(RunConfig, cl.user_session.get("config"))

    try:
        await on_agent_start_handler(history)

        # Add user message to history
        history.append({"role": "user", "content": message.content})

        # Get final reply from helper
        full_reply = await get_streamed_reply(agent, history, config)

        # Stream token by token
        for token in full_reply:
            await msg.stream_token(token)

        msg.content = full_reply
        history.append({"role": "assistant", "content": msg.content})
        cl.user_session.set("chat_history", history)

        # Validate and update final message
        msg.content = validate_agent_output(msg.content)
        await msg.update()

        # ✅ Save to MongoDB
        chat_collection.insert_one({
            "user_message": message.content,
            "assistant_reply": msg.content,
            "timestamp": datetime.utcnow()
        })

        await on_agent_end_handler(msg.content)

    except Exception as e:
        msg.content = f"❌ Error: {str(e)}"
        await msg.send()
        print(f"Error: {str(e)}")
