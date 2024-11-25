import requests
from bs4 import BeautifulSoup
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
# }
# response=requests.get("https://books.toscrape.com/catalogue/page-3.html",headers=headers)
# # response.encoding = response.apparent_encoding  # 自动检测编码

# soup=BeautifulSoup(response.text,"html.parser")

# # 找到价格
# # all_prices = soup.find_all("p",attrs={"class":"price_color"})
# # for price in all_prices:
#     # print(price.text)

# # 找到书名
# all_titles=soup.find_all("h3")
# for title in all_titles:
#     all_links=title.find("a")
#     # for link in all_titles:
#     #     print(link.string)
#     print(all_links.string)
    
import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# 循环分页爬取
for i in range(100):
    response = requests.get(
        f"https://www.chyxx.com/search?word=%E6%88%BF%E5%9C%B0%E4%BA%A7&cid=guandian&page={i}",
        headers=headers
    )

    # 解析HTML内容
    soup = BeautifulSoup(response.text, "html.parser")

    # 查找所有符合条件的标题
    all_titles = soup.find_all("h3", attrs={"class": "cx-media__title t-19 l-28 t-justify"})
    
    # 遍历并打印 href 内容
    for title in all_titles:
        link = title.find("a", href=True)  # 查找 <a> 标签
        if link:
            print(f"https://www.chyxx.com/{link['href']}")  # 打印 href 内容
