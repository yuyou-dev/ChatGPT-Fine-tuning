from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("CUSTOM_ENV_NAME")
)
client_file = client.files.create(
    file=open("../data/processed/chat_data.jsonl", "rb"),
    purpose="fine-tune"
)
print(client_file)