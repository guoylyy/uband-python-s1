#!/bin/usr/python
# -*- coding: utf-8 -*-
#@author:SKY

import os
import codecs
from wordcloud import WordCloud 
import matplotlib.pyplot as plt  
from PIL import Image
import numpy as np


class WordReader():

	def word_reader(self,file_path):
		fp=codecs.open(file_path,'r','utf-8')
		words=fp.read()
		return words
	

def main():
	wr=WordReader()
	# wlist=wr.word_reader('data1/dt01.txt')

	wcount=''
	for root,dirs,files in os.walk('data2'):
		for file in files:
			file_path=os.path.join(root,file)
			wlist=wr.word_reader(file_path)
			wcount+=wlist

	back_coloring = np.array(Image.open("./sky.png"))
	wc = WordCloud(
                background_color="white", #背景颜色  
                max_words=1000,# 词云显示的最大词数  
                mask=back_coloring,#设置背景图片  
                max_font_size=150, #字体最大值  
                random_state=42,  
                )
                
	wc.generate(wcount) 
	# 
	# wc.generate_from_frequencies(word_list)
	# wc.fit_words(word_list)
	plt.figure() 
	plt.imshow(wc)  
	plt.axis("off")
	plt.show()  




if __name__ == "__main__":
    main()
