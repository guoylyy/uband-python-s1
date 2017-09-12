#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: suancaiyu
#学习bool型数据代表的意义  True, False
def main():
  number = 1
  number_2 = 1.5

  string = '我是郭叔叔'

  is_cheap = False  #  boolean型表示
  is_cheap_2 = True
  

  if number >= number_2:  #分支判断
    print string
  else:
    print '错了%f错了' %(number_2)

if __name__ == '__main__':
	main()
