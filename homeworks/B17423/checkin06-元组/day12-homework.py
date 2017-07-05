#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

def main():
  tup = (1,2,3,4)

  #取值
  print (tup[0])
  # 切片
  print (tup)
  print (tup[0:2])
  print (tup[1:])
  
  # 是否存在某值
  print (1 in tup)
  print (0 in tup)

  # 赋值
  (a,b,c,d) = tup
  print (a)
  print (b)
  print (c)
  print (d)

  
  # 遍历
  print ("---iterate---")
  for x in tup:
    print (x)
  
  print ("---enumerate--")
  for index,item in enumerate(tup):
    print (index)

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  print ("---error---")
  try:
    # tup.append(5)  #插入 'tuple' object has no attribute 'append'
    # tup[0]=2    #修改 'tuple' object does not support item assignment
    # del tup[0]    #删除 'tuple' object doesn't support item deletion

  except Exception as e:
    print (e)
  
if __name__ == '__main__':
  main()


