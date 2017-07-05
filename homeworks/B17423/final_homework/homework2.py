#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya
# 词云生成

from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
#import pickle  #持久化对象
import jieba
import codecs
#import os

def main():
    file = open('data1/dt01.txt','rb').read()
   # text = pickle.load(file)
    file_after_jieba = jieba.cut(file, cut_all = True)
    text = " ".join(file_after_jieba)

    background_Image = plt.imread('data1/back.JPG')
    my_wordcloud = WordCloud(background_color = 'black',
    				mask = background_Image,
    				max_words = 50,    #最大显示的字数
    				# stopwords = STOPWORDS,
    				max_font_size =550,  #字体最大值
    				random_state = 30,  #多少种随机生成状态
    				scale = .5
    				)
    my_wordcloud.generate(text)
    image_colors = ImageColorGenerator(background_Image)
    my_wordcloud.recolor(color_func = image_colors)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
