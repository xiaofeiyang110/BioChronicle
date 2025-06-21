# BioChronicle 人物传记生成系统

BioChronicle 是一个基于大模型的自动人物传记生成工具，支持输入人名或网址，自动抓取资料、结构化信息提取、事实核查、文章生成和配图，适合自媒体、内容创作等场景。

## 功能特色

- 支持输入人名或百科网址，自动抓取和解析人物资料
- 多大模型适配（OpenAI、通义千问、火山引擎等），可配置切换
- 自动结构化信息抽取与事实核查
- 生成风格化、分章节的人物传记文章
- 自动生成配图，支持多种图片生成引擎
- 支持自定义文章风格、图片风格等

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourname/BioChronicle.git
cd BioChronicle
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# 安装依赖
pip install -r requirements.txt
```

### 3. 配置 API 密钥

编辑 `config/default.yaml`，填写你自己的 OpenAI、通义千问、火山引擎等 API 密钥。

### 4. 运行主程序

```bash
python src/main.py
```

根据提示输入人名或百科网址，系统会自动生成传记和配图，结果保存在 `output.md`。

## 主要目录结构

```
BioChronicle/
├── src/
│   ├── main.py                # 主程序入口
│   ├── core/                  # 主要业务逻辑（内容抓取、信息抽取、文章生成等）
│   └── adapters/              # 各类大模型和图片引擎适配器
├── config/
│   └── default.yaml           # 配置文件（模型、API密钥、风格等）
├── requirements.txt           # 依赖包列表
└── README.md
```

## 配置说明

- `config/default.yaml` 可配置大模型类型、API密钥、图片风格、文章风格等。
- 支持多种大模型和图片生成引擎，按需切换。

## 依赖环境

详见 `requirements.txt`，主要依赖：
- langchain
- langchain-openai
- langchain_community
- dashscope
- newspaper3k
- duckduckgo-search
- requests
- beautifulsoup4
- pyyaml
- python-dotenv
- lxml_html_clean
- tiktoken

## 常见问题

- 若抓取内容为空，建议检查网络或目标网址结构。
- 若图片未生成，请检查 API 密钥和配额，或查看调试输出。
- 若遇到模型相关报错，请确认配置文件和依赖包版本。

## License

MIT
