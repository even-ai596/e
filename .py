import requests
from bs4 import BeautifulSoup

def scrape_target_paragraphs(url):
    try:
        # 发送 HTTP 请求
        response = requests.get(url)
        response.raise_for_status()

        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找特定标签和样式
        target_paragraphs = soup.find_all('div', style=lambda value: value and 'rich_media_wrp' in value)

        # 提取文本内容
        extracted_texts = [paragraph.get_text(strip=True) for paragraph in target_paragraphs]

        return extracted_texts

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return []
    except Exception as e:
        print(f"其他错误: {e}")
        return []

# 示例用法
if __name__ == "__main__":
    # 替换为目标网页 URL
    target_url = "https://mp.weixin.qq.com/s?__biz=MzU5ODU1Mjg5Nw==&mid=2247766809&idx=4&sn=fe0c6d3eae9efe701b864a7fa5f5e1f0"

    # 爬取指定段落内容
    texts = scrape_target_paragraphs(target_url)

    # 输出结果
    if texts:
        print("爬取到的段落内容：")
        for text in texts:
            print(text)
    else:
        print("未找到匹配的段落内容。")
