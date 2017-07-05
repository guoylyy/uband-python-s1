#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[1:3]
  # 是否存在某值
  print (1 in tup)
  print (3 in tup)
  
  # 赋值
  a,b,c,d = tup
  print a
  print b
  print c
  print d
  # 遍历
  for index, item in enumerate(tup):
    print index
    print item
  for item in tup:
    print item


  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(9)
    tup[1] = 5
    del tup[0]

    
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


