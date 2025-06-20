import requests
import json
import time
from .base_adapter import BaseImageAdapter

class VolcEngineImageAdapter(BaseImageAdapter):
    def generate(self, prompt: str) -> str:
        access_key = self.config.get('volc_access_key')
        secret_key = self.config.get('volc_secret_key')
        
        if not access_key or not secret_key:
            return ""
        
        # 获取临时token
        token = self._get_volc_token(access_key, secret_key)
        if not token:
            return ""
        
        # 调用图片生成API
        url = "https://maas-api.ml-platform-cn-beijing.volces.com/image"
        
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "stable-diffusion-xl",
            "parameters": {
                "prompt": prompt,
                "width": 1024,
                "height": 1024,
                "style": self.config.get('image_style', '历史油画风'),
                "num_images": 1
            }
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            result = response.json()
            return result['images'][0]['url']
        except Exception as e:
            print(f"火山引擎图片生成失败: {e}")
            return ""
    
    def _get_volc_token(self, access_key: str, secret_key: str) -> str:
        """获取火山引擎临时token"""
        url = "https://open.volcengineapi.com/?Action=AssumeRole&Version=2021-06-01"
        
        payload = {
            "DurationSeconds": 3600,
            "RoleSessionName": "biochronicle-app"
        }
        
        try:
            response = requests.post(url, auth=(access_key, secret_key), json=payload)
            response.raise_for_status()
            result = response.json()
            return result['Result']['Credentials']['SessionToken']
        except Exception as e:
            print(f"火山引擎Token获取失败: {e}")
            return ""
    
    def get_engine_name(self):
        return "火山引擎Stable Diffusion"