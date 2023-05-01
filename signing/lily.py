from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import os
from dotenv import load_dotenv

import datetime
import pandas
import time

driver = webdriver.Chrome("./chrome/chromedriver.exe")

# -------- 連結到300登入介面 ------ #
driver.get("https://bbs.yamibo.com/plugin.php?id=zqlj_sign")
time.sleep(2)
# -------- 輸入帳密並登入 ------ #
load_dotenv(encoding="utf-8") # 載入.env

driver.find_elements(By.NAME, "username")[0].send_keys(os.getenv('300_NAME'))
driver.find_elements(By.NAME, "password")[0].send_keys(os.getenv('PASSWORD'))
driver.find_element(By.NAME, "loginsubmit").click()
time.sleep(7)

# -------- 簽到 ------ #
driver.find_element(By.XPATH, '//*[@id="wp"]/div[2]/div[2]/div[1]/a').click()
time.sleep(1)
driver.quit()

# -------- 輸出上次運行時間以確認是否有正常運行 ------ #
now = datetime.datetime.now()
txt = '上次運行時間為：' + str(now)

# 轉成df
df = pandas.DataFrame([txt], index=['UpdateTime'])

# 存出檔案
df.to_csv('300_log.txt', header=False)i