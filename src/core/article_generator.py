from langchain.prompts import ChatPromptTemplate
from adapters.llm.llm_factory import LLMFactory
from utils.config_loader import get_config
from utils.style_transfer import apply_style  # 修复导入

def generate_article(info):
    """生成传记文章"""
    base_prompt = """
    你是一位资深传记作家。请根据以下信息创作一篇引人入胜的自媒体文章：
    
    人物信息：
    - 出生年份: {birth_year}
    - 重要事件: {key_events}
    - 重要影响: {influences}
    - 奇闻趣事: {anecdotes}
    
    要求：
    1. 标题吸引人（使用emoji和悬念）
    2. 按时间线叙述（分3-5个章节）
    3. 每章结尾设悬念
    4. 融入至少1个趣闻
    5. 结尾引发讨论（提问式结尾）
    """
    
    # 应用风格配置
    full_prompt = apply_style(base_prompt)
    
    # 准备数据
    data = {
        "birth_year": info.get("birth_year", "未知"),
        "key_events": "\n- ".join(info.get("key_events", [])),
        "influences": "\n- ".join(info.get("influences", [])),
        "anecdotes": "\n- ".join(info.get("anecdotes", []))
    }
    
    # 获取模型适配器
    config = get_config()
    model_config = config.get('model', {})
    llm_adapter = LLMFactory.get_adapter(model_config)
    
    # 生成文章
    llm = llm_adapter.get_llm()
    prompt_template = ChatPromptTemplate.from_template(full_prompt)
    chain = prompt_template | llm
    result = chain.invoke(data)
    
    print(f"使用模型: {llm_adapter.get_model_name()}")
    return result.content