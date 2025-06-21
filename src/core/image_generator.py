from adapters.image.image_factory import ImageFactory
from utils.config_loader import get_config
from utils.style_transfer import get_image_style  # 修复导入

def generate_images(article):
    """根据文章内容生成图片"""
    # 1. 创建图片提示词
    prompts = create_image_prompts(article)
    print(f"[DEBUG] prompts: {prompts}")
    
    # 2. 使用配置的引擎生成图片
    config = get_config()
    image_config = config.get('image', {})
    
    # 合并API密钥
    api_keys = config.get('api_keys', {})
    image_config.update(api_keys)
    
    # 获取图片适配器
    image_adapter = ImageFactory.get_adapter(image_config)
    print(f"[DEBUG] image_adapter: {image_adapter.get_engine_name()}")
    
    # 生成图片
    image_urls = []
    
    for prompt in prompts:
        url = image_adapter.generate(prompt)
        print(f"[DEBUG] prompt: {prompt}, url: {url}")
        if url:
            image_urls.append(url)
    
    print(f"使用图片引擎: {image_adapter.get_engine_name()}")
    return image_urls

def create_image_prompts(article):
    """从文章中提取图片提示词"""
    # 获取配置的图片风格
    style = get_image_style()
    
    # 简单实现：将文章分成段落，每个段落生成一个提示词
    paragraphs = [p for p in article.split("\n\n") if len(p) > 50]
    prompts = []
    
    for i, para in enumerate(paragraphs[:5]):  # 最多5张图片
        # 提取关键内容
        content = extract_key_content(para)
        
        prompt = f"{style}，描绘: {content}"
        prompts.append(prompt)
    
    return prompts

def extract_key_content(text: str, max_length: int = 200) -> str:
    """从文本中提取关键内容"""
    # 简单实现：取文本开头
    return text[:max_length]