
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

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
driver.maximize_window()

# 打开目标页面
url = 'https://www.767stock.com/searchinfo'  # 替换为目标网页的 URL
driver.get(url)

# 等待页面加载完成
time.sleep(2)

# 打开文件以写入 URL
with open("urls.txt", "w") as file:
    
    # 获取所有标题元素
    links = driver.find_elements(By.CSS_SELECTOR, 'p.item-title.limit1')  # 根据截图中的选择器

    # 遍历每个标题并点击
    for i, link in enumerate(links):
        try:
            # 使用 ActionChains 模拟点击
            ActionChains(driver).move_to_element(link).click(link).perform()
            
            # # 等待新页面加载
            # time.sleep(2)  # 根据页面加载速度适当调整

            # 切换到新打开的标签页
            driver.switch_to.window(driver.window_handles[-1])
            
            # 获取当前页面的 URL 和内容
            current_url = driver.current_url
            page_content = driver.page_source
            print(f"第 {i+1} 个页面 URL: {current_url}")
            
            # 将 URL 写入文件
            file.write(current_url + "\n")
            
            # 关闭当前标签页并切换回主页面
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"第 {i+1} 个链接出现错误: {e}")
            driver.switch_to.window(driver.window_handles[0])  # 切换回主页面

# 关闭 WebDriver
driver.quit()
print("所有 URL 已保存到 urls.txt 文件中")


