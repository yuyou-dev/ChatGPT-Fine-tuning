import json
import random

raw_data = []
with open('../data/raw/test_datasets.jsonl', 'r') as file:
    for line in file:
        item = json.loads(line)
        raw_data.append(item)

# 随机从6000条数据中取出100条做训练测试
raw_messages = random.sample(raw_data,100)

with open('../data/processed/chat_data.jsonl', 'w') as data_file:
    for item in raw_messages:
        # 初始化消息对象
        data = {"messages": []}
        data["messages"].append({"role": "system", "content": "你是一个医疗助手"})
        data["messages"].append({"role": "user", "content": item["questions"]})
        data["messages"].append({"role": "assistant", "content": item["answers"]})
        result = {"messages": data}
        json.dump(result, data_file, ensure_ascii=False)
        data_file.write('\n')
