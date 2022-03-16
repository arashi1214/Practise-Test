import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

content = open('corpus.txt', 'r', encoding='utf-8').read()

wordlist_after_jieba = jieba.cut(content, cut_all = False)

'''
a = []
for w in jieba.cut(content, cut_all = False):
    a.append(w)
'''
    
wl_space_split = " ".join(wordlist_after_jieba)
print(wl_space_split)

chi_font='NotoSerifCJKtc-SemiBold.otf' #中文字型

wordcloud = WordCloud(font_path = chi_font,         \
                      background_color = "black",   \
                      max_words = 100,              \
                      width = 1000, height = 860).generate(wl_space_split) 


plt.imshow(wordcloud)    #繪製圖片
plt.axis("off")          #不顯示尺規座標
plt.show()               #顯示圖片
wordcloud.to_file("testpic.png")