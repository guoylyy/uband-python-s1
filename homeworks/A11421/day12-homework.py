#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[0]
  # 切片
  tup2 = tup[1:3]
  print tup2
  # 是否存在某值
  print (1 in tup)
  print (1 in tup2)
  # 赋值
  a,b,c,d = tup
  print a
  print b
  print c
  print d
  # 遍历
  

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    # tup[0] = 1
    # tup.append(9)
   del tup[0]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


