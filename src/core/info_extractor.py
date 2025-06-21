from langchain_core.pydantic_v1 import BaseModel, Field
from adapters.llm.llm_factory import LLMFactory
from utils.config_loader import get_config

class InfoSchema(BaseModel):
    birth_year: int = Field(..., description="出生年份")
    key_events: list[str] = Field(..., description="重要事件列表")
    influences: list[str] = Field(default_factory=list, description="重要影响人物或事件")
    anecdotes: list[str] = Field(default_factory=list, description="奇闻趣事")

def extract_info(text):
    """从文本中提取结构化信息（新版LangChain推荐方式）"""
    config = get_config()['model']
    llm = LLMFactory.get_adapter(config).get_llm()
    llm_structured = llm.with_structured_output(InfoSchema)
    result = llm_structured.invoke(text)
    return result.dict() if hasattr(result, 'dict') else result