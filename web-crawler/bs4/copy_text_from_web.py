import requests
import re
from bs4 import BeautifulSoup
from opencc import OpenCC # 簡繁轉換

st = 1 # 默認從第一章開始下載
web = input("請輸入小說目錄網址：")
chose = eval(input('請選擇要全部章節下載還是範圍章節下載：\n1) 全部章節下載\n2) 範圍章節下載\n'))

if chose == 1:
	chapter = eval(input("請輸入可閱讀的總共篇數："))
else:
	st = eval(input("請輸入從第幾章開始下載："))
	chapter = eval(input("請輸入下載到第幾章："))

savefile = input("請輸入要存放的資料夾名稱（必須已存在）：")

for i in range(st, chapter + 1):
	#url = 'http://www.jjwxc.net/onebook.php?novelid=3477117&chapterid=1'
	url = web + "&chapterid=" + str(i)

	res = requests.get(url)
	res.encoding = "utf-8"
	soup = BeautifulSoup(res.content, "lxml")

	try:
		titie = soup.find("h2").get_text()
	except:
		continue
	novel = soup.select(".noveltext")[0].text # 等同於get_text()
	index = novel.find("查看收藏列表")
	novel = novel[index+15:]

	for char in '。 ”':
		if char == "。":
			novel = novel.replace(char,"。\n")
		elif char == "”":
			novel = novel.replace(char,"”\n")
		else:
			novel = novel.replace(char,"")
	titie = OpenCC('s2tw').convert(titie)
	novel = OpenCC('s2tw').convert(novel)

	file = open('./' + savefile + '/' + str(i) + '.' + titie + '.txt','w', encoding="utf-8")
	file.write(novel)
	file.close()
print("存檔完畢")