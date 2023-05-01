import requests
import re
import xlrd
import xlwt
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup

open_file_name = input("請輸入要讀取的excel檔：")
file_name = input("請輸入要存檔的檔名(不用打副檔名)：")

# from trips.models import Information
driverPath = r"D:\chromedriver.exe"
driver = webdriver.Chrome(driverPath)

driver.get("https://read.moe.edu.tw/web-sso/rest/Redirect/login/page/normal?returnUrl=https://read.moe.edu.tw/WebAuth.do")
#print(driver.title) # 輸出網頁標題

# 登入
driver.find_element_by_name("username").send_keys('')
driver.find_element_by_name("password").send_keys('')
driver.find_element_by_id("btn-submit").click()
# 進入全國圖書館
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modarea"]/div[3]/a[1]/div'))).click()

# 輸入索書號(打開讀取的excel檔案)
indexs = xlrd.open_workbook(open_file_name)
nrow = indexs.sheets()[0].nrows
ncol = indexs.sheets()[0].ncols
indexbook = xlwt.Workbook() # 建立excel
worksheet = indexbook.add_sheet('test') #建立資料表
# 分類號、作者號、年代號(民國)、部冊號、登陸號
worksheet.write(0, 0, '分類號')
#indexbook.save('excelwrite.xls')

worksheet.write(0, 1, '作者號')
#indexbook.save('excelwrite.xls')

worksheet.write(0, 2, '年代號(民國)')
#indexbook.save('excelwrite.xls')

worksheet.write(0, 3, '部冊號')
#indexbook.save('excelwrite.xls')

worksheet.write(0, 4, '登陸號')
#indexbook.save('excelwrite.xls')
label = 0
for i in range(nrow): # 總行數
	for j in range(ncol): #總列數
		try:
			Classification_number = ""
			Au_number = ""
			year = ""
			Part_number = ""
			Login_number = ""

			driver.implicitly_wait(15)
			number = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="libportal"]/div/div/div/ng-include/div[2]/ng-include/div/div[2]/div/div[1]/div/div[1]/div[2]/input'))) 
			#print(indexs.sheets()[0].cell(i,j).value) #輸出對應的行列值
			number.clear() # 清空輸入框
			number.send_keys(indexs.sheets()[0].cell(i,j).value) # 輸入索書號
			# 點擊搜尋
			WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="libportal"]/div/div/div/ng-include/div[2]/ng-include/div/div[2]/div/div[1]/div/div[1]/div[2]/ul/li[1]/a'))).click()
			# 載入書籍
			WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ambryListModal"]/div/div[2]/ng-include/div/div[2]/div[2]/div/ul/li[1]/div[2]/a'))).click()

			# 取得書標資訊
			driver.implicitly_wait(25)

			windows=driver.window_handles
			driver.switch_to.window(windows[-1])

			Classification_number = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[5]/span[2]').text
			Au_number = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[5]/span[4]').text

			if driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[7]/span[1]').text == "出版項：":
				year = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[7]/span[2]').text
			elif driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[9]/span[1]').text == "出版項：":
				year = driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[9]/span[2]').text
			else:
				print("年代出錯誤，請檢查', i+1,',',j+1,'欄位的書目資料")
			Login_number = indexs.sheets()[0].cell(i,j).value

			#抓取登陸號對應的冊次與複本號
			for m in range(1,100):
				try:
					print('/html/body/div/div[2]/div[2]/ul[' + str(m) + ']/li[1]')
					
					if driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/ul[' + str(m) + ']/li[1]').text == Login_number:
						Part_number = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/ul[' + str(m) + ']/li[3]').text + driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/ul[' + str(m) + ']/li[4]').text
						break
				except:
					print("找不到對應的登入號：", Login_number)

			st = -1
			#抓取民國年代
			for k in range(len(year)):
				if year[k] == "民國" or year[k] == "民":
					st = k+1
				elif year[k] == ']':
					en = k

			worksheet.write(label+1, 0, Classification_number)
			indexbook.save(file_name + '.xls')
		
			worksheet.write(label+1, 1, Au_number)
			indexbook.save(file_name + '.xls')

			if st != -1:
				worksheet.write(label+1, 2, '民' + year[st:en])
				indexbook.save(file_name + '.xls')

			worksheet.write(label+1, 3, Part_number)
			indexbook.save(file_name + '.xls')

			worksheet.write(label+1, 4, Login_number)
			indexbook.save(file_name + '.xls')

			label += 1

			driver.close()
			driver.switch_to.window(windows[0])
			driver.find_element_by_xpath('//*[@id="ambryListModal"]/div/div[2]/button').click()
		except:
			print('出現問題')
			print('請檢查', i+1,',',j+1,'欄位的書目資料')
			sys.exit()
