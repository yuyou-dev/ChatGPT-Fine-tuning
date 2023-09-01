
# 创建微调模型
import requests
import json
#这里需要写自己的key
api_key = ''
#这里需要写upload_data后返回的file_id
file_id = ''

url = "https://api.openai.com/v1/fine_tuning/jobs"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "training_file": f"{file_id}",
    "model": "gpt-3.5-turbo-0613"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)
response_json = json.loads(response.text)  # 将响应文本转换为 JSON 字典
fine_tuning_job_id = response_json["id"]
print(fine_tuning_job_id) #当前微调模型的id，可用于后续查看模型的状态