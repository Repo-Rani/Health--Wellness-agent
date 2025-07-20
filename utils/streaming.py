# stream_utils.py
from agents import Runner
from typing import Any

async def get_streamed_reply(agent, history, config) -> str:
    result = Runner.run_streamed(agent, history, run_config=config)
    full_reply = ""

    async for event in result.stream_events():
        if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
            token = event.data.delta
            full_reply += token

    return full_reply
