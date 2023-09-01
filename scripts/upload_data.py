# 上传数据 上传jsonl文件
import requests
import json
#这里需要写自己的key
api_key = ''
#这里写jsonl数据文件的地址
data_path = "../data/processed/chat_data.jsonl"

url = "https://api.openai.com/v1/files"
headers = {
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "purpose": "fine-tune",
}
files = {
    "file": open(f"{data_path}", "rb")
}

response = requests.post(url, headers=headers, data=payload, files=files)
response_text = response.text
print(response_text)
response_json = json.loads(response_text)  # 将响应文本转换为 JSON 字典
file_id = response_json["id"]
print(file_id) #获取到具体的文件名，用于下一步的微调任务
