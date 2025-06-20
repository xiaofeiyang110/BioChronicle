try:
    from langchain_community.chat_models.volcengine_maas import VolcEngineMaasChat
except ImportError:
    # 兼容旧版本LangChain
    from langchain_community.chat_models import VolcEngineMaasChat

from .base_adapter import BaseLLMAdapter

class DoubaoModelAdapter(BaseLLMAdapter):
    def get_llm(self):
        return VolcEngineMaasChat(
            model=self.config.get('doubao_model', 'doubao-1.6'),
            volc_engine_access_key=self.config.get('volc_access_key'),
            volc_engine_secret_key=self.config.get('volc_secret_key'),
            region=self.config.get('volc_region', 'cn-beijing'),
            temperature=0.7,
            top_p=0.8
        )
    
    def get_model_name(self):
        return f"字节豆包: {self.config.get('doubao_model', 'doubao-1.6')}"