from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 Chrome 选项
options = Options()
options.binary_location = "chrome_for_testing/chrome"  # 替换为 Chrome for Testing 的实际路径
options.add_argument("headless")  # 无头模式
options.add_argument("disable-gpu")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")

# 设置 chromedriver 路径
driver_path = 'chromedriver-linux64/chromedriver'  # 替换为 chromedriver 的实际路径
service = Service(driver_path)

# 初始化 Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.767stock.com/searchinfo")

# 使用显式等待，等待页面加载并确保元素可见
wait = WebDriverWait(driver, 10)  # 等待最多10秒
try:
    # 等待并找到所有包含标题的元素
    elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p.item-title.limit1')))
    
    # 打开文件以写入符合条件的标题
    with open("titles.txt", "w", encoding="utf-8") as file:
        for element in elements:
            # 获取标题文本
            title_text = element.text  # 使用 .text 属性提取文本
            if "房地产" in title_text:  # 如果标题包含“房地产”
                # 将标题文本写入文件
                file.write(title_text + "\n")
                print(f"已保存标题: {title_text}")
except Exception as e:
    print(f"出现错误: {e}")

# 关闭 WebDriver
driver.quit()

print("所有包含 '房地产' 的标题已保存到 titles.txt 文件中")
