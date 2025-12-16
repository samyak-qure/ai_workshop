from portkey_ai import Portkey
import os
from dotenv import load_dotenv

load_dotenv()

portkey_api_key = os.environ.get("PORTKEY_API_KEY")
provider_name = "openrouter-09cb28"
portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)


response = portkey_client.chat.completions.create(
    model="openai/gpt-4.1-mini", messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, How are you?"}
    ], cache=False
)
print(response.choices[0].message.content)