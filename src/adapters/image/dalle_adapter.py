from openai import OpenAI
from .base_adapter import BaseImageAdapter

class DalleAdapter(BaseImageAdapter):
    def generate(self, prompt: str) -> str:
        client = OpenAI(api_key=self.config.get('openai_api_key'))
        
        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            return response.data[0].url
        except Exception as e:
            print(f"DALL-E 图片生成失败: {e}")
            return ""
    
    def get_engine_name(self):
        return "OpenAI DALL-E 3"