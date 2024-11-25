import requests
from bs4 import BeautifulSoup

# 目标页面的URL
url = 'https://www.chyxx.com/wiki/1199965.html'

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

# 发送请求获取页面内容
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析页面
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 定位包含目标文本的div标签
    content_div = soup.find('div', class_='diwiki-article_body mb-32')  # 根据页面结构调整类名
    
    # 提取并打印红框内的文本内容
    if content_div:
        text = content_div.get_text(separator='\n', strip=True)
        print("红框内的文本内容:\n")
        print(text)
    else:
        print("未找到指定的内容，请检查类名或结构。")
else:
    print("请求失败，请检查URL或请求头。")
