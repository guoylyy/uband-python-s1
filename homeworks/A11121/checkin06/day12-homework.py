#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[2]

  # 切片
  print tup[1:4]
  print tup[2:]
  print tup
  # 是否存在某值
  print (5 in tup)

  # 赋值
  a, b, c, d =(1,2,3,4)
  print '----'
  print a
  print a,b
 
  # 遍历
  for item in tup:
    print item
  for index, item in enumerate(tup):
    print index

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
     tup[3] = 8
  except Exception, e:
    print e

  try:
    tup.append(8)
  except Exception,e:
    print e

  
if __name__ == '__main__':
  main()


