# -*- coding: utf-8 -*-
import json
import random

def transform_jsonl(input_file_path, output_file_path):
    entries = []
    with open(input_file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            entries.append(entry)

    # 随机抽取100个条目
    sampled_entries = random.sample(entries, 100)

    with open(output_file_path, 'w') as outfile:
        for entry in sampled_entries:
            messages = []
            messages.append({"role": "system", "content": "你是一个医疗助手"})
            user_message = {"role": "user", "content": entry["questions"]}
            assistant_message = {"role": "assistant", "content": entry["answers"]}
            messages.extend([user_message, assistant_message])
            result = {"messages": messages}
            json.dump(result, outfile, ensure_ascii=False)
            outfile.write('\n')

# 准备好的txt文件
input_file_path = "../data/raw/test_datasets.jsonl"
# 需要输出的jsonl文件地址
output_file_path = "../data/processed/chat_data.jsonl"

transform_jsonl(input_file_path, output_file_path)