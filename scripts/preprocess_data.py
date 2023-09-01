# 把txt文件处理成我们需要的jsonl的形式
import json
# 准备好的txt文件
input_path = "../data/raw/training_data.txt"
# 需要输出的jsonl文件地址
output_path = "../data/processed/chat_data.jsonl"

# 打开文件
with open(f'{input_path}', 'r', encoding='utf-8') as file:
    content = file.read()
# 以三个连续的换行符分割成段落
paragraphs_level1 = content.split('\n\n\n')

# 构建消息列表
messages = []

for i, paragraph_level1 in enumerate(paragraphs_level1, start=1):
    # 在每个段落内再以两个连续的换行符分割内容
    paragraphs_level2 = paragraph_level1.split('\n\n')

    # 初始化消息对象
    message = {"messages": []}

    # 添加系统消息
    message["messages"].append({"role": "system", "content": "你是一名翻译"})

    # 添加第二级段落内容到不同角色的消息
    for j, paragraph_level2 in enumerate(paragraphs_level2, start=1):
        role = "user" if j % 2 == 1 else "assistant"
        message["messages"].append({"role": role, "content": paragraph_level2})

    # 将消息对象添加到消息列表
    messages.append(message)

# 将消息列表写入到 chat_data.jsonl 文件
with open(f'{output_path}', 'w', encoding='utf-8') as jsonl_file:
    for message in messages:
        jsonl_file.write(json.dumps(message, ensure_ascii=False) + '\n')
