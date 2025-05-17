import json
import random
from pathlib import Path

# Base directory of this script file so we can build absolute paths. This
# allows the script to run correctly even when executed from other
# directories.
BASE_DIR = Path(__file__).resolve().parent

raw_data = []
raw_data_path = BASE_DIR.parent / 'data' / 'raw' / 'test_datasets.jsonl'
with open(raw_data_path, 'r', encoding="utf-8") as file:
    for line in file:
        item = json.loads(line)
        raw_data.append(item)

# 随机从6000条数据中取出100条做训练测试
raw_messages = random.sample(raw_data,100)

# 按OpenAI数据规范，将训练数据按行整理成JSON-L文件
processed_path = BASE_DIR.parent / 'data' / 'processed' / 'chat_data.jsonl'
with open(processed_path, 'w', encoding="utf-8") as data_file:
    for item in raw_messages:
        data = {"messages": []}
        data["messages"].append({"role": "system", "content": "你是一个医疗助手"})
        data["messages"].append({"role": "user", "content": item["questions"]})
        data["messages"].append({"role": "assistant", "content": item["answers"]})
        json.dump(data, data_file, ensure_ascii=False)
        data_file.write('\n')
