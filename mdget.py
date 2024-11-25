# import requests
# from bs4 import BeautifulSoup
# import csv
# import re
# import time  # 引入 time 模块

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
# }

# # 修改正则表达式以匹配中文、英文、数字及常见标点符号
# pattern = re.compile(r'[\u4e00-\u9fffA-Za-z0-9.%\-，。！、？：；“”‘’\'"()\[\]{}]')

# # 打开文件并逐行读取 URL
# with open("links.txt", "r", encoding="utf-8") as file:
#     urls = file.readlines()

# # 以追加模式打开文件，避免覆盖之前的内容
# with open("智研咨询_EDA软件.md", "w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
    
#     for url in urls:
#         url = url.strip()  # 去掉多余的空格或换行符
#         try:
#             response = requests.get(url, headers=headers, timeout=10)  # 发送请求，设置超时
#             response.raise_for_status()  # 检查请求是否成功
#             soup = BeautifulSoup(response.text, "html.parser")

#             # 查找所有 <p> 标签
#             all_titles = soup.find_all("p")

#             # 提取并写入包含中英文的文本内容
#             for title in all_titles:
#                 # 使用正则表达式筛选需要的内容
#                 filtered_text = ''.join(pattern.findall(title.get_text()))
#                 if filtered_text:  # 仅写入有内容的部分
#                     print(filtered_text)
#                     writer.writerow([filtered_text])
            
#             # 每次爬取完一个 URL 后，延迟 5 秒
#             time.sleep(1)
#         except requests.exceptions.RequestException as e:
#             print(f"无法处理 URL {url}: {e}")
import requests
from bs4 import BeautifulSoup
import re
import time  # 引入 time 模块
import os  # 用于操作文件夹

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
}

# 修改正则表达式以匹配中文、英文、数字及常见标点符号
pattern = re.compile(r'[\u4e00-\u9fffA-Za-z0-9.%\-，。！、？：；“”‘’\'"()\[\]{}]')

# 目标文件夹路径
output_folder = "智研咨询_光伏组件"

# 如果目标文件夹不存在，则创建文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开文件并逐行读取 URL
with open("links.txt", "r", encoding="utf-8") as file:
    urls = file.readlines()

# 记录文件编号
file_index = 1

for url in urls:
    url = url.strip()  # 去掉多余的空格或换行符
    try:
        response = requests.get(url, headers=headers, timeout=10)  # 发送请求，设置超时
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.text, "html.parser")

        # 查找所有 <p> 标签
        all_titles = soup.find_all("p")

        # 准备写入的文件名和路径
        output_file_name = f"智研咨询_光伏组件_{file_index:02d}.md"
        output_file_path = os.path.join(output_folder, output_file_name)

        # 提取并写入包含中英文的文本内容
        with open(output_file_path, "w", encoding="utf-8", newline="") as file:
            for title in all_titles:
                # 使用正则表达式筛选需要的内容
                filtered_text = ''.join(pattern.findall(title.get_text()))
                if filtered_text:  # 仅写入有内容的部分
                    print(filtered_text)
                    file.write(filtered_text + "\n")

        print(f"内容已写入文件: {output_file_path}")
        file_index += 1  # 文件编号递增

        # 每次爬取完一个 URL 后，延迟 1 秒
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"无法处理 URL {url}: {e}")
