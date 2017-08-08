#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: fangcheng
 
def main():
  tup = (4,5,6,7)
 
  #取值
  print tup[1]
  # 切片
  print tup
  print tup[1:3]
  print tup[2:]
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
   
  # 赋值
  a,b,c,d = (4,5,6,4)
  print a
  print b
  print c
  print d
  # 遍历
  print '****'
  for item in tup:
    print item
  
  print 'enumerate---'
  for index ,item in enumerate(tup):
  	print index
 
  # 花式报错

  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(9)
    #del tup[0]
    tup[0] = 'aaa'
  except Exception, e:
    print e
   
if __name__ == '__main__':
  main()