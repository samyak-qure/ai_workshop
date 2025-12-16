from portkey_ai import Portkey
import os
from dotenv import load_dotenv

load_dotenv()

def call_llm(messages: list[dict]):
    portkey_api_key = os.environ.get("PORTKEY_API_KEY")
    provider_name = "openrouter-09cb28"
    portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)
    response = portkey_client.chat.completions.create(
        model="google/gemini-2.5-flash", messages=messages, cache=False
    )

    return response.choices[0].message.content