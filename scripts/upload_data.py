import requests
import json

api_key = ''                                       #填写从开发者后台获取的api_key
data_path = "../data/processed/chat_data.jsonl"    #处理完的数据路径

url = "https://api.openai.com/v1/files"            #上传文件的api        
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
print(response_text)                               # 查看相应结果
response_json = json.loads(response_text)          # 将响应文本转换为 JSON 字典
file_id = response_json["id"]
print(file_id)                                     #上传成功，获取文件id
