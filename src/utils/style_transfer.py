import re
from utils.config_loader import get_config

def apply_style(base_prompt: str) -> str:
    """
    应用配置的风格到提示词
    
    参数:
        base_prompt: 基础提示词模板
        
    返回:
        应用风格后的完整提示词
    """
    # 获取风格配置
    style_config = get_config().get('style', {})
    article_config = style_config.get('article', {})
    
    # 构建风格描述
    style_desc = ""
    if article_config.get('tone'):
        style_desc += f"采用{article_config['tone']}的写作风格，"
    if article_config.get('length'):
        style_desc += f"字数约{article_config['length']}字，"
    
    # 添加参考文章
    ref_content = ""
    if article_config.get('examples'):
        ref_content = "\n\n### 参考文章片段:\n"
        for example in article_config['examples']:
            # 简化和清理参考文章
            cleaned_example = clean_text(example)
            ref_content += f"- {cleaned_example[:200]}...\n"
    
    # 添加结构要求
    structure_requirements = ""
    if article_config.get('structure'):
        structure_requirements = "\n\n### 结构要求:\n"
        structure_requirements += f"- 文章应包含 {article_config['structure']['sections']} 个主要章节\n"
        structure_requirements += f"- 每章节长度约 {article_config['structure']['section_length']}\n"
    
    # 组合完整提示词
    full_prompt = (
        f"{base_prompt}"
        f"\n\n### 风格要求:\n{style_desc.strip()}"
        f"{ref_content}"
        f"{structure_requirements}"
    )
    
    # 清理多余的空行
    full_prompt = re.sub(r'\n{3,}', '\n\n', full_prompt)
    return full_prompt.strip()

def clean_text(text: str) -> str:
    """清理文本中的多余空格和换行"""
    # 替换多个连续空格为单个空格
    text = re.sub(r' +', ' ', text)
    # 替换多个连续换行为单个换行
    text = re.sub(r'\n+', '\n', text)
    # 删除开头和结尾的空格
    return text.strip()

def get_image_style() -> str:
    """获取配置的图片风格"""
    image_config = get_config().get('image', {})
    return image_config.get('style', '历史插画风格')