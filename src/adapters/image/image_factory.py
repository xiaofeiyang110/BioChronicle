from .dalle_adapter import DalleAdapter
from .tongyi_adapter import TongyiImageAdapter
from .volcengine_adapter import VolcEngineImageAdapter
from .base_adapter import BaseImageAdapter

class ImageFactory:
    """图片生成工厂类"""
    ADAPTER_MAP = {
        "dalle": DalleAdapter,
        "tongyi": TongyiImageAdapter,
        "volcengine": VolcEngineImageAdapter
    }
    
    @classmethod
    def get_adapter(cls, config: dict) -> BaseImageAdapter:
        """根据配置获取适配器实例"""
        engine = config.get('engine', 'dalle')
        adapter_class = cls.ADAPTER_MAP.get(engine)
        
        if not adapter_class:
            raise ValueError(f"不支持的图片引擎: {engine}")
        
        return adapter_class(config)