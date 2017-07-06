#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小白

def main():
  tup = (1,2,3,4,5,7,9)

  #取值
  print tup[5]
  # 切片
  print tup[0:5]
  # 是否存在某值
  print (1 in tup)
  print (6 in tup)
  # 赋值
  q, w, e, r = (1,2,3,4)
  print e
  print r
  print '__________'
  # 遍历
  index = 0
  for tup_item in tup:
     print tup_item
  index = index +1
  print '_________'
  #tup.append(6)
  #tup[3] = '666'
  #del tup[2]
  print '________________-'
  #try:
    #del tup[2]
  #except tup[2], e:
    #print e
  
if __name__ == '__main__':
  main()
