from langchain_openai import ChatOpenAI
from utils.config_loader import get_config

def get_llm():
    """获取配置的LLM实例"""
    config = get_config()
    model_type = config['model']['llm']
    
    if model_type == "openai":
        return ChatOpenAI(model=config['model']['openai_model'])
    else:
        # 默认使用OpenAI
        return ChatOpenAI(model="gpt-4-turbo")