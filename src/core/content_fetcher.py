from newspaper import Article
from langchain_community.tools import DuckDuckGoSearchRun
from utils.config_loader import get_config

def fetch_content(input_type, content):
    """根据输入类型获取内容"""
    if input_type == "url":
        return fetch_url_content(content)
    else:
        return fetch_name_content(content)

def fetch_url_content(url):
    """获取URL内容"""
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def fetch_name_content(name):
    """搜索人名获取内容"""
    search = DuckDuckGoSearchRun()
    query = f"{name} 维基百科 生平"
    result = search.run(query)
    return result[:5000]  # 限制长度