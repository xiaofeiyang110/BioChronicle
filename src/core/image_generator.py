from adapters.image_adapter import get_image_engine
from utils.config_loader import get_config

def generate_images(article):
    """根据文章内容生成图片"""
    # 1. 创建图片提示词
    prompts = create_image_prompts(article)
    
    # 2. 使用配置的引擎生成图片
    engine = get_image_engine()
    image_urls = []
    
    for prompt in prompts:
        image_url = engine.generate(prompt)
        if image_url:
            image_urls.append(image_url)
    
    return image_urls

def create_image_prompts(article):
    """从文章中提取图片提示词"""
    # 简单实现：将文章分成段落，每个段落生成一个提示词
    paragraphs = [p for p in article.split("\n\n") if len(p) > 50]
    prompts = []
    
    for i, para in enumerate(paragraphs[:5]):  # 最多5张图片
        prompt = f"{get_config()['image']['style']}风格，描绘: {para[:200]}"
        prompts.append(prompt)
    
    return prompts