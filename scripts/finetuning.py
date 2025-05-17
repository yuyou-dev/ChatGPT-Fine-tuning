from openai import OpenAI
import os
from pathlib import Path

client = OpenAI(
    api_key=os.environ.get("CUSTOM_ENV_NAME")
)

# ID of the uploaded training file. The upload step returns this ID.
training_file_id = ''  # TODO: replace with your uploaded file ID

file_tuning_job = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model="gpt-3.5-turbo",
)
print(file_tuning_job)
