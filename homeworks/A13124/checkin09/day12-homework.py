#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  tup1 = tup[1]
  print tup1
  # 切片
  print tup[1:3]
  # 是否存在某值
  print (1 in tup)
  # 赋值
  a,b,c,d = tup
  print a
  print b
  print c
  print d
  # 遍历
  for item in tup:
    print item
  for index,item in enumerate(tup):
    print index,item

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup[0]=3
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


