#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#text = open(path.join(d, 'constitution.txt')).read()
def get_file_from_folder(folder_path):
    file_paths = []
    #root-当前目录位置 dirs-当前目录中目录 files-当前文件 
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root,file) #位置-文件名
            file_paths.append(file_path)
    print ("扫描到%d个文件"%(len(file_paths)))
    return file_paths

def read_files(file_paths):
    text = ""
    for file_path in file_paths:
        text = text + codecs.open(file_path).read()
    return text

def generate_wordcloud(text):
    wordcloud = WordCloud(max_font_size=40).generate(text)
    wordcloud.to_file(png_path)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print ("done!")
    
def main():
    file_paths = get_file_from_folder(folder_path)
    text = read_files(file_paths)
    generate_wordcloud(text)
    
if __name__ == "__main__":
    folder_path = "./data2"     #should modify
    png_path = "./output/wordcloud.png"
    main()
