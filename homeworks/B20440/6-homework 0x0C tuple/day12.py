#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

def main():
  tup = (1,2,3,4)
  print tup[1]
  print tup
  print tup[2:4]
  
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
  
  # 赋值
  a,b,c,d = (1,2,3,4)
  print a
  print b
  print c
  print d
  
  print '---'
  
  for index, item in enumerate(tup):
    print index
    print '---'
    print item

  print '---'
  try:
    tup.append(9) 
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()