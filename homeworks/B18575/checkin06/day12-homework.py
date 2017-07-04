#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: SKY

def main():
  tup = (1,2,3,4)

  #取值
  print tup[0]
  # 切片
  print tup[1:3]
  print tup[2:]
  # 是否存在某值
  print (1 in tup)
  print (6 in tup)
  
  # 赋值
  a,b,c=(2,3,4)
  print a,b,c
  
  # 遍历
  for i in tup:
  	print i
  

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    # tup.append(2)
    # tup[2]=9
    # del tup[2]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


