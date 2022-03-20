from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv

import datetime
import pandas


# -------- 以不顯示瀏覽器的方式啟動 ------ #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 啟動無頭模式
chrome_options.add_argument('--disable-gpu') # windowsd必須加入此行


# -------- 確認 chromedriver 版本 ------ #
try:
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chrome/chromedriver.exe")
except:
	import chrome_helper
	chrome_helper.check_browser_driver_available()
	driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chrome/chromedriver.exe")

# -------- 連結到金石堂登入介面 ------ #
driver.get("https://www.kingstone.com.tw/login")


# -------- 輸入帳密並登入 ------ #
load_dotenv(encoding="utf-8") # 載入.env

driver.find_element(By.NAME, "loginID").send_keys(os.getenv('ACCOUNT'))
driver.find_element(By.NAME, "loginPW").send_keys(os.getenv('PASSWORD'))

driver.find_element_by_class_name("inLGbtn").click()

# -------- 切到會員介面並簽到 ------ #
driver.get("https://www.kingstone.com.tw/ksmember/home/")

driver.find_element_by_class_name("calender").click()
driver.quit()

# -------- 輸出上次運行時間以確認是否有正常運行 ------ #
now = datetime.datetime.now()
txt = '上次運行時間為：' + str(now)

# 轉成df
df = pandas.DataFrame([txt], index=['UpdateTime'])

# 存出檔案
df.to_csv('log.txt', header=False)