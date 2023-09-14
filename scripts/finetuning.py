import requests
import json

api_key = ''                                # 从开发者后台获取的api_key
file_id = ''                                # 从file接口返回的文件id

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
print(response.text)                        # 查看响应内容
response_json = json.loads(response.text)   # 将响应文本转换为 JSON 字典
fine_tuning_job_id = response_json["id"]    # 获取微调任务id
print(fine_tuning_job_id)                   # 当前微调模型的id，可用于后续查看模型的状态
