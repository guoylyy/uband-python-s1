#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wangxiangchun

def main():
  dictionary = {
                'good':'of a  favorable charachter or tendency',
                'none':'not any such thing or person',
                'nice':'very beautiful'
               }
  print len(dictionary) #长度
  #获得key的列表
  print dictionary.keys() 
  #获得value的列表
  print dictionary.values()
  #是不是在
  print dictionary.has_key('good')
  print dictionary.has_key('bad')

  #add
  dictionary['bad'] = "not very good"
  print dictionary
  print len(dictionary)

  #modify
  dictionary['bad'] = "failing to reach an acceptable standard"
  print dictionary

  #delete
  del dictionary['bad']

  print dictionary
  print len(dictionary)

  #get value 
  print '--------'
  print dictionary['good']
  if dictionary.has_key('bad'):
    print dictionary['bad']
  #iterator 
  for key in dictionary.keys():
    print key
    print dictionary[key]


if __name__ == '__main__':
  main()
