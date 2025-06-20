from langchain_community.chat_models.tongyi import ChatTongyi
from .base_adapter import BaseLLMAdapter

class TongyiModelAdapter(BaseLLMAdapter):
    def get_llm(self):
        return ChatTongyi(
            model_name=self.config.get('tongyi_model', 'qwen-max'),
            dashscope_api_key=self.config.get('dashscope_api_key'),
            temperature=0.7,
            top_p=0.8
        )
    
    def get_model_name(self):
        return f"通义千问: {self.config.get('tongyi_model', 'qwen-max')}"