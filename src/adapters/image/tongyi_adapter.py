import requests
import json
from .base_adapter import BaseImageAdapter

class TongyiImageAdapter(BaseImageAdapter):
    def generate(self, prompt: str) -> str:
        api_key = self.config.get('dashscope_api_key')
        if not api_key:
            return ""
        
        url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "wanx-v1",
            "input": {
                "prompt": prompt
            },
            "parameters": {
                "style": self.config.get('image_style', '水墨风'),
                "size": "1024*1024",
                "n": 1
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result['output']['results'][0]['url']
        except Exception as e:
            print(f"通义万相图片生成失败: {e}")
            return ""
    
    def get_engine_name(self):
        return "通义万相"