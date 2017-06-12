#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  dictionary = {
                'good':'of a favorable character or tendenc',
                'none': 'not any such thing or person',
                'nice': 'very beautiful'
               }
  
  print len(dictionary) #长度
  #获得keys
  print dictionary.keys() #获取key的列表

  #获得value
  print dictionary.values() #获取vlaues的列表

  #是不是在
  print dictionary.has_key('good') #有
  print dictionary.has_key('bad') #没有

  #add
  dictionary['bad'] = "not very good"

  #modify
  dictionary['bad'] = "failing to reach an acceptable standard "
  print dictionary
  
  #delete
  del dictionary['bad']
  print dictionary
  print len(dictionary)

  # get value
  print '---'
  print dictionary['good']
  if dictionary.has_key('bad'):
    print dictionary['bad'] #这一段没执行
  else:
    print '没有 bad 这个单词'
  print '---'

  # iterator
  for key in dictionary.keys():
    print key
    print dictionary[key]

if __name__ == '__main__':
  main()