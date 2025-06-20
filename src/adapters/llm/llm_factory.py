from .openai_adapter import OpenAIModelAdapter
from .tongyi_adapter import TongyiModelAdapter
from .doubao_adapter import DoubaoModelAdapter

class LLMFactory:
    """大模型工厂类"""
    ADAPTER_MAP = {
        "openai": OpenAIModelAdapter,
        "tongyi": TongyiModelAdapter,
        "doubao": DoubaoModelAdapter
    }
    
    @classmethod
    def get_adapter(cls, config: dict) -> BaseLLMAdapter:
        """根据配置获取适配器实例"""
        provider = config.get('provider', 'openai')
        adapter_class = cls.ADAPTER_MAP.get(provider)
        
        if not adapter_class:
            raise ValueError(f"不支持的模型提供商: {provider}")
        
        return adapter_class(config)