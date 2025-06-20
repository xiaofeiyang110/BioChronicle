from abc import ABC, abstractmethod
from langchain_core.language_models import BaseLanguageModel

class BaseLLMAdapter(ABC):
    """大模型适配器基类"""
    def __init__(self, config: dict):
        self.config = config
    
    @abstractmethod
    def get_llm(self) -> BaseLanguageModel:
        """获取LangChain兼容的LLM实例"""
        pass
    
    @abstractmethod
    def get_model_name(self) -> str:
        """获取模型名称"""
        pass