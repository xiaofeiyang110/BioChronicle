from dotenv import load_dotenv
load_dotenv()  # 加载环境变量

from core.input_router import route_input
from core.content_fetcher import fetch_content
from core.info_extractor import extract_info
from core.fact_checker import verify_events
from core.article_generator import generate_article
from core.image_generator import generate_images
from utils.config_loader import get_config

def main():
    print("=== BioChronicle 人物传记生成系统 ===")
    user_input = input("请输入人名或网址: ")
    
    # 1. 输入路由
    input_type, content = route_input(user_input)
    print(f"输入类型: {input_type}")
    
    # 2. 获取内容
    raw_content = fetch_content(input_type, content)
    print(f"获取内容成功! 长度: {len(raw_content)}字符")
    
    # 3. 信息提取
    extracted_info = extract_info(raw_content)
    print(f"提取信息: {extracted_info}")
    
    # 4. 事实核查
    if get_config()['verification']['enabled']:
        verified_events = verify_events(extracted_info['key_events'])
        extracted_info['verified_events'] = verified_events
        print("事实核查完成!")
    
    # 5. 生成文章
    article = generate_article(extracted_info)
    print(f"文章生成成功! 长度: {len(article)}字符")
    
    # 6. 生成图片
    image_urls = generate_images(article)
    print(f"生成 {len(image_urls)} 张图片")
    
    # 7. 保存结果
    save_output(article, image_urls, extracted_info)
    print("结果已保存到 output.md")

def save_output(article, image_urls, info):
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(article + "\n\n")
        
        # 添加事实核查信息
        if 'verified_events' in info:
            f.write("## 事实核查\n")
            for event in info['verified_events']:
                f.write(f"- {event['event']} (置信度: {event['confidence']:.2f}, 来源: {', '.join(event['sources'])})\n")
            f.write("\n")
        
        # 添加图片
        f.write("## 生成图片\n")
        for i, url in enumerate(image_urls):
            f.write(f"![图片 {i+1}]({url})\n\n")

if __name__ == "__main__":
    main()