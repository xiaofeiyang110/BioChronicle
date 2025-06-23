from dotenv import load_dotenv
load_dotenv()  # 加载环境变量

from core.article_generator import generate_article_from_name
from core.fact_checker import verify_events
from core.image_generator import generate_images
from utils.config_loader import get_config

def main():
    print("=== BioChronicle 人物传记生成系统 ===")
    user_input = input("请输入人名: ")

    # 1. 直接根据名称输出自媒体文章
    article = generate_article_from_name(user_input)
    print(f"文章生成成功! 长度: {len(article)}字符")
    print(article)

    # 2. 针对文章进行事实核查
    verified_events = []
    if get_config()['verification']['enabled']:
        verified_events = verify_events(article)
        print("事实核查完成!")

    # 3. 生成图片
    image_urls = generate_images(article)
    print(f"生成 {len(image_urls)} 张图片")

    # 4. 保存结果
    save_output(article, image_urls, {"verified_events": verified_events})
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