from pypinyin import pinyin, lazy_pinyin
import pypinyin

word = input()
# style為中文轉換結果的設定，例如注音，羅馬拼音....

dic = {
	"ㄅ" : "1",
	"ㄆ" : "q",
	"ㄇ" : "a",
	"ㄈ" : "z",
	"ㄉ" : "2",
	"ㄊ" : "w",
	"ㄋ" : "s",
	"ㄌ" : "x",
	"ˇ" : "3",
	"ㄍ" : "e",
	"ㄎ" : "d",
	"ㄏ" : "c",
	"ˋ" : "4",
	"ㄐ" : "r",
	"ㄑ" : "f",
	"ㄒ" : "v",
	"ㄓ" : "5",
	"ㄔ" : "t",
	"ㄕ" : "g",
	"ㄖ" : "b",
	"ˊ" : "6",
	"ㄗ" : "y",
	"ㄘ" : "h",
	"ㄙ" : "n",
	"˙" : "7",
	"ㄧ" : "u",
	"ㄨ" : "j",
	"ㄩ" : "m",
	"ㄚ" : "8",
	"ㄛ" : "i",
	"ㄜ" : "k",
	"ㄝ" : ",",
	"ㄞ" : "9",
	"ㄟ" : "o",
	"ㄠ" : "l",
	"ㄡ" : ".",
	"ㄢ" : "0",
	"ㄣ" : "p",
	"ㄤ" : ";",
	"ㄥ" : "/",
	"ㄦ" : "-"
}


while word != "exit":
	pinyin(word, style=pypinyin.BOPOMOFO)
	pin_yin = pinyin(word, style=pypinyin.BOPOMOFO)
	reply = ""
	for i in pin_yin:
		for j in i:
			if j[-1] not in ["ˊ", "ˇ", "ˋ", "˙"]:
				j = j + " "
			for k in j:
				if k in dic:
					reply = reply + dic[k]
				else:
					reply = reply + k

	print(reply)
	word = input()