from langchain_openai import ChatOpenAI
from .base_adapter import BaseLLMAdapter

class OpenAIModelAdapter(BaseLLMAdapter):
    def get_llm(self):
        return ChatOpenAI(
            model=self.config.get('openai_model', 'gpt-4-turbo'),
            temperature=0.7
        )
    
    def get_model_name(self):
        return f"OpenAI: {self.config.get('openai_model', 'gpt-4-turbo')}"