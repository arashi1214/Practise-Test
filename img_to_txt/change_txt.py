from PIL import Image


def image_to_txt(imgName, maxSize):
	print("開啟圖片[{}]".format(imgName))
	try:
		img = Image.open(imgName )
	except:
		print("開啟圖片[{}}時出現錯誤".format(imgName))

	#確定圖片資訊
	print("圖片資訊： 大小為{}x{}, 格式為{}, 色彩模式為{}".format(img.size[0], img.size[1], img.format, img.mode))
	#確定圖片顏色編碼
	if img.mode != 'RGB':
		print("圖片顏色編碼不是RGB，進行轉換")
		img = img.convert("RGB")
		print("轉換完成")

	width = img.size[0]
	height = img.size[1]

	zoom = 0
	if width >= maxSize:
		zoom = width / maxSize
		width = int(width / zoom)
		height = int(height / zoom)
		height = int(height / 2)
		img = img.resize((width, height))
		print("圖片寬於{}，已縮小為{}x{}".format(maxSize, img.size[0], img.size[1]))


	img = img.convert('1')

	namestr = imgName.split('.')[0] + '.txt'
	txt = open(namestr, 'w')
	print()
	print("開始進行圖片轉txt程序")
	print("...")
	for y in range(height):
		for x in range(width):
			pixel = img.getpixel((x,y))

			if pixel != 0:
				txt.write(' ')
			else:
				txt.write('@')
		txt.write("\n")

	print("程序執行完成")
	print("檔案程序為[{}]".format(namestr))
	txt.close()
	print("檔案完成")

name = input("請輸入檔案名稱，圖片須放置於同一層資料夾：")
maxSize = int(input("請輸入最大寬度(100~500)："))
if maxSize < 100 or maxSize > 500:
	print("輸入錯誤")
else:
	image_to_txt(name, maxSize)
print("程式結束")

"""
轉角度
img = Image.open('joy_cat.jpg') #放入檔名
img = img.rotate(-90)  #看要轉幾度
img.save('rotate.jpg') #儲存的檔名 
"""
