from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

def verify_events(events):
    """对事件进行多源验证"""
    verified_events = []
    
    # 初始化工具
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    
    for event in events:
        sources = []
        
        # 使用维基百科验证
        try:
            result = wikipedia.run(f"{event} 事实核查")
            if "不存在" not in result and "未找到" not in result:
                sources.append("维基百科")
        except:
            pass
        
        # 简单置信度计算
        confidence = min(1.0, len(sources) / 2)  # 最多0.5，留出空间给其他来源
        
        verified_events.append({
            "event": event,
            "sources": sources,
            "confidence": confidence
        })
    
    return verified_events