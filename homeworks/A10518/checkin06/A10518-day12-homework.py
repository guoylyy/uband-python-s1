#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (5,6,7,8)

  #取值
  print tup[1]
  # 切片
  print tup[2:]
  # 是否存在某值
  print (1 in tup)
  # 赋值
  w,x,y,z = (5,6,7,8)
  print w
  # 遍历
  for item in tup:
    print item

  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(1) 
    del tup[0]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


