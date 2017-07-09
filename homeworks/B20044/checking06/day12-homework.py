#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():


  tup = (1,2,3,4)

  #取值
  print tup [1] #忘了写print   1代表的是下标index
  print tup [2]

  # 切片
  print tup[1:3]
  print tup[:5]


  # 是否存在某值
  print (3 in tup)
  print (7 in tup)

  # 赋值
  a,b,c=tup[1:4]
  print a 
  print b 
  print c 

#列表也可以
  # lst=[1,2]
  # x=lst[1]
  # print x



  print'-----'
  # 遍历
  for item in tup:
  	print item 

  print'-----'
  for index,item in enumerate(tup):
  	print index
  	print item



  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  #前面并不一定要写一个raise exception的程序 
  try:
   # tup.append(10)
  #  tup[1]='aaa'
   del tup [1]


  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


