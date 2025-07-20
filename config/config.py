import os
from dotenv import load_dotenv

from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


load_dotenv()

# 🔹 Environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")
base_url = os.getenv("GEMINI_API_URL")
model_name = os.getenv("GEMINI_API_MODEL")

# 🔹 Client setup
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= base_url,

)
#  🔹 Model setup
model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model = str(model_name)
)

# 🔹 Run configuration
run_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True

)