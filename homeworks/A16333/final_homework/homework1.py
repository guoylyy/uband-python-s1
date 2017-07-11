# -*- coding: utf-8 -*-

import codecs
import os

#
# 程度较好的同学可以不看 tips.py
#


def get_file_from_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
    	wenjian = []
        for file in files:
            file_path = os.path.join(root, file)
            wenjian.append(file_path)
    print wenjian

          
    return wenjian


def read_file(file_path):
  f = codecs.open(file_path, 'r', "utf-8")
  lines = f.readlines()
  word_list = []
  for line in lines:
    line = line.strip()
    words = line.split(" ")
    word_list.extend(words)




def main():

  get_file_from_folder('data')
  

  

  



 
 


if __name__ == '__main__':
  main()            