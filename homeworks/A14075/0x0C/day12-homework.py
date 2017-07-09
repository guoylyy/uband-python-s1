#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (11,22,33,44)

  #取值
  print (tup[0])
  
  # 切片
  tup1 = tup[1:-1]
  print (tup1)
  
  # 是否存在某值
  print (1 in tup)
  print (0 in tup)
  
  # 赋值
  a,b,c,d = tup
  print (a,b,c,d)
  
  # 遍历
  for item in tup:
      print (item)
  
  for index,item in enumerate(tup):
      print (index,item)

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
   # tup.append(1)
   # tup[0]=1
    del tup[0]
  except Exception as e:
    print (e)
  
if __name__ == '__main__':
  main()


