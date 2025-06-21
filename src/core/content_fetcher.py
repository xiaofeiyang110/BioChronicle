import requests
from bs4 import BeautifulSoup
from newspaper import Article
from langchain_community.tools import DuckDuckGoSearchRun
from utils.config_loader import get_config

def fetch_content(input_type, content):
    """根据输入类型获取内容"""
    if input_type == "url":
        text = fetch_url_content(content)
        print(f"[DEBUG] 获取到的URL内容：{text[:500]}...")
        return text
    else:
        text = fetch_name_content(content)
        print(f"[DEBUG] 获取到的人名内容：{text[:500]}...")
        return text

def fetch_url_content(url):
    """获取URL内容"""
    if "baike.baidu.com" in url:
        return fetch_baike_content(url)
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def fetch_baike_content(url):
    """优先API，失败则爬虫"""
    text = fetch_baike_by_api(url)
    if text:
        print("[DEBUG] 通过API获取到百度百科内容")
        return text
    print("[DEBUG] API获取失败，尝试爬虫方式……")
    return fetch_baike_by_crawler(url)

def fetch_baike_by_api(url):
    """预留百度百科API获取实现，返回空字符串表示失败"""
    # 示例：如有API可在此实现
    # api_url = f"https://api.baidu.com/baike?url={url}&apikey=YOUR_API_KEY"
    # try:
    #     resp = requests.get(api_url, timeout=10)
    #     if resp.status_code == 200:
    #         data = resp.json()
    #         return data.get("summary", "")
    # except Exception as e:
    #     print(f"[DEBUG] API异常: {e}")
    return ""

def fetch_baike_by_crawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    print(f"[DEBUG] 状态码: {resp.status_code}, 内容长度: {len(resp.text)}")
    resp.encoding = resp.apparent_encoding
    soup = BeautifulSoup(resp.text, "html.parser")
    print("[DEBUG] 页面部分HTML:", soup.prettify()[:1000])
    content_div = soup.find("div", class_="lemmaWrapper_ICvAM")
    if not content_div:
        content_div = soup.find("div", class_="lemmaWgt-lemmaSummary")
    print(f"[DEBUG] content_div 是否找到: {content_div is not None}")
    if content_div:
        text = content_div.get_text(separator="\n", strip=True)
        return text
    return ""

def fetch_name_content(name):
    """搜索人名获取内容"""
    search = DuckDuckGoSearchRun()
    query = f"{name} 维基百科 生平"
    result = search.run(query)
    return result[:5000]  # 限制长度