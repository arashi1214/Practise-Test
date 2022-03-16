import os
import time
import requests
from bs4 import BeautifulSoup

if not os.path.exists("images"):
    os.mkdir("images")  # 建立資料夾

url = 'https://www.wikiart.org/en/pablo-picasso/all-works/text-list'
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')

name = soup.find_all("li", class_="painting-list-text-row")
number = 1

for i in name:
    print(number)
    picture_url = "https://www.wikiart.org/" + i.a.get('href')
    picture_response = requests.get(picture_url)
    picture_response.encoding = 'utf-8'
    
    picture_soup = BeautifulSoup(picture_response.text, 'html.parser')
    img = picture_soup.find_all("img", {'itemprop':"image"})
    input_image = i.a.text.replace('"', " ")
    
    for j in img:
        img = requests.get(j.get('src'))  # 下載圖片
        with open('images\\' + str(number) + "."  + input_image + '.jpg', 'wb') as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼
    number += 1
    time.sleep(2)
print("end")