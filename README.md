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
│   └── finetuning_demo.ipynb
│
├── .gitignore
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
python preprocess_data.py
```

### Upload Data / 上传数据
Run the upload script:
```bash
python upload_data.py
```

### Fine-tuning / 微调训练
Run the fine-tuning script:
```bash
python finetuning.py
```

## Running Tests / 验证和测试

Run API test on [PlayGround](https://platform.openai.com/playground)

## Contributing / 贡献

We welcome contributions! Please open an issue or submit a pull request on GitHub.
我们欢迎各种贡献！请在GitHub上开启一个问题(issue)或提交一个拉取请求(pull request)。

## License / 许可

[MIT License](LICENSE)

