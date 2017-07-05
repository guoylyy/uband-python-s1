#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

#字典报错

def main():
  dictionary = {
  				'good' : 'of a favorable character or tendency',
  				'none' : 'not any such thing or person',
  				'nice' : 'very beautiful'
  				}

  #长度
  print (len(dictionary))

  #获得keys
  print (dictionary.keys())

  #获得values
  print (dictionary.values())

  #是不是在
  try:
  	print (dictionary.has_key('good'))
  except Exception as e:
  	print ("error:%s" % e)  #error:'dict' object has no attribute 'has_key'

  try:
  	for key in dictionary.keys:
  		print (key,':',dictionary[key])  #error:'builtin_function_or_method' object is not iterable
  except Exception as e:
  	print ("error:%s" % e)
  

  print ('good' in dictionary)
  print ('bad' in dictionary)

if __name__ == '__main__':
	main()