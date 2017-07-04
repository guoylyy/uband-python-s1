#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import collections

def read_word(path): 
	file_open = open(path,'r')
	file_content = file_open.read().decode('utf-8')
	file_word = file_content.split(" ") #分行
   	fmt = 'abcdefghijklmnopqrstuvwxyz-'
   	for i in range(len(file_word)):
   		for char in file_word[i]:
   			if char not in fmt:
   				file_word[i] = file_word[i].lower().replace(char,'')
  	count = {}
   	for word in file_word:
   		if not count.has_key(word):
   			count[word] = 1
   		else:
   			count[word] = count[word] + 1
   	count = collections.OrderedDict(sorted(count.items(), key=lambda t: -t[1]))
   	return count
def print_to_csv(count, path): #输出CSV
	nfile = open(path,'w+')
	for key in count.keys():
		val = count[key]
		nfile.write("%s,%s\n" % (key, str(val)))
	nfile.close()

def get_file_from_folder(folder_path): #读取文件夹中的文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
        	file_path = os.path.join(root, file)

        	return file_path

from os import path
from wordcloud import WordCloud
d = path.dirname('C:\Users\geniu\Documents\uband-python-s1\\final-homework\data2')
text = open(path.join(d, 'C:\Users\geniu\Documents\uband-python-s1\\final-homework\output\\test.csv')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

def main():
	a = get_file_from_folder('data2')
   	count = read_word(a)
	print_to_csv(count,'C:\Users\geniu\Documents\uband-python-s1\\final-homework\output\\test.csv')
if __name__ == "__main__":
    main()

