#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

#作业1:对照 day9 字典学习 打一遍代码
#词典：包含大括号，key,values,各种功能学习,注意 2.7和3.5的区别

def homework1():
  dictionary = {
                'good':'of a favorable character or tendenc',
                'none':'not any such thing or person',
                'nice':'very beautiful'
               }
  print (len(dictionary))  # get length 
  print (dictionary.keys())  #get keys
  print (dictionary.values()) #get values
  #zhao keys 
  if ('good' in dictionary.keys() ):
    print ('dictionary has good')
  if ('bad' in dictionary.keys()):
  	print('TRUE')
  else:
    print('FALSE')
  print('-----')
  #add
  dictionary['bad'] = 'not very good thing'   
  print (dictionary)
  #modify
  dictionary['bad'] = "failing to reach an acceptable standard "
  print (dictionary)
  print('____')
  #delete
  del dictionary['good']
  print (dictionary)
  print (len(dictionary))
 # iterator
  for key in dictionary.keys():
    print (key)
    print (dictionary[key])
if __name__ == '__main__':
  homework1()