from langchain.chains import create_extraction_chain
from adapters.llm_adapter import get_llm

def extract_info(text):
    """从文本中提取结构化信息"""
    schema = {
        "properties": {
            "birth_year": {"type": "integer", "description": "出生年份"},
            "key_events": {"type": "array", "items": {"type": "string"}, "description": "重要事件列表"},
            "influences": {"type": "array", "items": {"type": "string"}, "description": "重要影响人物或事件"},
            "anecdotes": {"type": "array", "items": {"type": "string"}, "description": "奇闻趣事"}
        },
        "required": ["birth_year", "key_events"]
    }
    
    llm = get_llm()
    chain = create_extraction_chain(schema, llm)
    result = chain.invoke({"input": text})
    
    # 返回第一个提取结果
    return result[0] if result else {
        "birth_year": None,
        "key_events": [],
        "influences": [],
        "anecdotes": []
    }