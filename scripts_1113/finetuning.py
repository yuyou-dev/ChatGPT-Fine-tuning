from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ.get("CUSTOM_ENV_NAME")
)
file_tuning_job = client.fine_tuning.jobs.create(
    training_file='',
    model="gpt-3.5-turbo"
)
print(file_tuning_job)