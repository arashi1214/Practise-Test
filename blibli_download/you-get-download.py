import os

def download_video(filename):
	file = open(filename, 'r', encoding="utf-8")

	for i in file:
	
		url = i.replace('\n', '')
		download = "you-get -l " + url
		os.system(download)



def write_txt():
	video = os.listdir()
	with open("merge.txt", 'w', encoding="utf-8") as merge_file:
		for d in video:
			if ".flv" in d:
				save_name = d.split(".")[0]
				merge_file.write("file '" + d + "'\n")
			elif '.mp4' in d:
				save_name = d.split(".")[0]
				write_name = d.replace('.download', '')
				os.rename('./' + d,'./' + write_name)
				merge_file.write("file '" + write_name + "'\n")

download_video('url_text.txt')
# ==== 有要多p合併的再使用下列的函式 ==== #
# write_txt()
# os.system("ffmpeg -f concat -safe 0 -i merge.txt -c copy output.mp4")
os.system("del *.xml")