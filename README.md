# ChatGPT-Fine-tuning / ChatGPT微调指南
Quick-start guide to fine-tuning ChatGPT using Python. Includes scripts for data preprocessing, model training, and evaluation. 

快速入门指南: 使用Python微调ChatGPT。包含数据预处理、模型训练和评估脚本。

## Project Structure / 项目结构

```
chatgpt-finetuning/
│
├── data/
│   ├── raw/
│   │   ├── training_data.txt
│   │   └── validation_data.txt
│   └── processed/
│       └── ...
│
├── scripts/
│   ├── preprocess_data.py
│   ├── upload_data.py
│   └── finetuning.py
│
├── notebooks/
│   ├── fine-tuning.ipynb
│   ├── fine-tuning-format.ipynb
│   ├── fine-tuning-format-comparison.ipynb
│   └── 视频解说.ipynb
│
├── README.md
└── requirements.txt
```

## Getting Started / 开始

1. **Clone the Repository / 克隆仓库**:
```bash
git clone https://github.com/yuyou-dev/chatgpt-fine-tuning.git
cd chatgpt-fine-tuning
```

2. **Install Dependencies / 安装依赖**:
```bash
pip install -r requirements.txt
```

3. **Fine-tuning the Model / 微调模型**:

Navigate to the `scripts/` directory and run the script to preprocess data:

### Preprocess Data / 预处理数据
```bash
python3 preprocess_data.py
```

### Upload Data / 上传数据
Run the upload script:
```bash
python3 upload_data.py
```

### Fine-tuning / 微调训练
Run the fine-tuning script:
```bash
python3 finetuning.py
```

## Running Tests / 验证和测试

Run API test on [PlayGround](https://platform.openai.com/playground)

## Colab 微调

- 1.[微调基础用例](https://colab.research.google.com/github/yuyou-dev/ChatGPT-Fine-tuning/blob/main/notebooks/fine-tuning.ipynb)
- 2.[微调实战-训练指定格式和字段的输出](https://colab.research.google.com/github/yuyou-dev/ChatGPT-Fine-tuning/blob/main/notebooks/fine-tuning-format.ipynb)
- 3.[微调实战-训练指定格式和字段的输出-不同方式的对比](https://colab.research.google.com/github/yuyou-dev/ChatGPT-Fine-tuning/blob/main/notebooks/fine-tuning-format-comparison.ipynb)

## 其他GPT技术
- 1.[GPT-4v实现AI视频解说 - Colab]([https://github.com/yuyou-dev/ChatGPT-Fine-tuning/blob/main/notebooks/视频解说.ipynb](https://colab.research.google.com/github/yuyou-dev/ChatGPT-Fine-tuning/blob/main/notebooks/video-commentary.ipynb))
  
## Contributing / 贡献

We welcome contributions! Please open an issue or submit a pull request on GitHub.
我们欢迎各种贡献！请在GitHub上开启一个问题(issue)或提交一个拉取请求(pull request)。

## License / 许可

[MIT License](LICENSE)

