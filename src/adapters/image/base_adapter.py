from abc import ABC, abstractmethod

class BaseImageAdapter(ABC):
    """图片生成适配器基类"""
    def __init__(self, config: dict):
        self.config = config
    
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """生成图片并返回URL"""
        pass
    
    @abstractmethod
    def get_engine_name(self) -> str:
        """获取引擎名称"""
        pass