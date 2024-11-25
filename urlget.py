# # import requests
# # from bs4 import BeautifulSoup
# # headers={
# #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
# # }
# # for num in range(0,1001):
# #     response=requests.get(f"https://www.fxbaogao.com/archives/industry/%E5%BB%BA%E7%AD%91%E5%BB%BA%E6%9D%90?page={num}",headers=headers)
# #     # response.encoding = response.apparent_encoding  # 自动检测编码
# #     # print(response.status_code)
# #     soup=BeautifulSoup(response.text,"html.parser")
# #     all_titles=soup.find_all("div",attrs={"class":"flex-11 flex-ccj"})
# #     for title in all_titles:
# #         obstract=title.find("a")
# #         link=title.find("a")["href"]
# #         print(obstract.string,f"https://www.fxbaogao.com{link}")
# import requests
# from bs4 import BeautifulSoup
# import csv

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
# }

# # Open a CSV file in write mode
# with open("output.txt", "w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     # Write header row
#     writer.writerow(["Title", "Link"])
    
#     for num in range(0, 1001):
#         response = requests.get(f"https://www.fxbaogao.com/archives/industry/%E5%BB%BA%E7%AD%91%E5%BB%BA%E6%9D%90?page={num}", headers=headers)
#         # response.encoding = response.apparent_encoding  # Auto-detect encoding if needed
#         soup = BeautifulSoup(response.text, "html.parser")
#         all_titles = soup.find_all("div", attrs={"class": "flex-11 flex-ccj"})
        
#         for title in all_titles:
#             obstract = title.find("a").string
#             link = title.find("a")["href"]
#             full_link = f"https://www.fxbaogao.com{link}"
#             # Write each title and link to a new row in the CSV file
#             writer.writerow([obstract, full_link])
import requests
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

# 打开文件，以写入模式保存数据
with open("links.txt", "w", encoding="utf-8") as file:
    # 循环分页爬取
    for i in range(100):
        response = requests.get(
            f"https://www.chyxx.com/search?word=%E5%85%89%E4%BC%8F%E7%BB%84%E4%BB%B6&cid=guandian&page={i}",
            headers=headers
        )

        # 解析HTML内容
        soup = BeautifulSoup(response.text, "html.parser")

        # 查找所有符合条件的标题
        all_titles = soup.find_all("h3", attrs={"class": "cx-media__title t-19 l-28 t-justify"})
        
        # 遍历并将 href 内容写入文件
        for title in all_titles:
            link = title.find("a", href=True)  # 查找 <a> 标签
            if link:
                full_link = f"https://www.chyxx.com{link['href']}"  # 构造完整链接
                file.write(full_link + "\n")  # 写入文件并换行
                print(full_link)  # 可选：同时打印在控制台，便于调试

