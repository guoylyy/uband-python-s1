# -*- coding: utf-8 -*-

import codecs
import os
from wordcloud import WordCloud 



#1.读入文件频率
# def read_cvs(file_path):
    
#     text = open(file_path).readlines()
#     #print text
        
#     return text
def read_file(file_path):
  f = codecs.open(file_path, 'r', "utf-8")
  lines = f.readlines()
  word_list = []
  for line in lines:
      line = line.strip()
      words = line.split(" ") #按照空格分割单词
      word_list.extend(words)
  return word_list


#2.清洗文档
def clean_text(text,text_narrow):
  text_frequency = {}
#print text
  for line in text:
     frenquency = line.split()
     for list in  frenquency:
       str(list)
       list_1 = list.split(',')
     #print list_1
       a = list_1[0]
       b = list_1[1]
       b = int (b)

       if a not in text_narrow:
          #if b < 6000:
         #print a 
         #print b
            text_frequency[a] = b   #词频6000以下的单词，如何删除常用词？
#print text_frequency.keys()
#print text_frequency.values()
  return text_frequency

#3.画图
def picture(text_frequency):
    wordcloud = WordCloud(background_color = "white",max_words=3000).generate_from_frequencies(text_frequency)
    
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    # # # lower max_font_size
    # #wordcloud = WordCloud(max_font_size=40).generate(text)
    # #plt.figure()
    # #plt.imshow(wordcloud, interpolation="bilinear")
    # #plt.axis("off")
    plt.show()

def main():
    text_1 = read_file('output/test.csv')
    text_2 = read_file('output/normalwords.txt')
    #print text_2
    #print text_1 
    #print text_2
    text_frequency_1 = clean_text(text_1,text_2)
    #print text_frequency_1
    picture(text_frequency_1)




if __name__ == '__main__':
    main()