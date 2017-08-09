#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: eros

def main():
  tup = (1,2,3,4)

  #取值
  print [2]
  print [4]
  # 切片
  print tup
  print tup[0:4]
  print tup[2:]
  # 是否存在某值
  print (1 in tup)
  print (40 in tup)
  # 赋值
  a,w,c,d= (1,2,3,4)
  print a
  print w
  print d
  print c

  print "=========="
  # 遍历
  for item in tup:
    print item
  for index,item in enumerate(tup):
    print index
    print item

  try:
    del tup[2]
  except Exception,e:  
    print e
  
if __name__ == '__main__':
  main()


