from openai import OpenAI
import os
from pathlib import Path

client = OpenAI(
    api_key=os.environ.get("CUSTOM_ENV_NAME")
)

# Path to the processed training data relative to this file so the script
# can be executed from any directory.
processed_path = Path(__file__).resolve().parent.parent / 'data' / 'processed' / 'chat_data.jsonl'

client_file = client.files.create(
    file=open(processed_path, 'rb'),
    purpose="fine-tune",
)
print(client_file)
