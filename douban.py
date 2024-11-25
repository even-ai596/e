import requests
from bs4 import BeautifulSoup
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
for num in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={num}&filter=",headers=headers)
    # response.encoding = response.apparent_encoding  # 自动检测编码
    # print(response.status_code)
    soup=BeautifulSoup(response.text,"html.parser")
    all_titles=soup.find_all("span",attrs={"class":"title"})
    for title in all_titles:
        if "/" not in title.string:
            print(title.string)