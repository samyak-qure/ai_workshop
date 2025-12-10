from portkey_ai import Portkey

portkey_api_key = "BYhj9/tYnCqhoFx7rSXIv6VSePmP"
provider_name = "openrouter-09cb28"
portkey_client = Portkey(api_key=portkey_api_key, virtual_key=provider_name)


response = portkey_client.chat.completions.create(
    model="google/gemini-2.5-flash", messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, How are you?"}
    ], cache=False
)
print(response.choices[0].message.content)