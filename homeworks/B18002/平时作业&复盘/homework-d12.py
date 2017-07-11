#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup[1:3]
  print tup[0:]
  
  # 是否存在某值
  print (1 in tup)
  print (6 in tup)
  # 赋值
  a, b, c, d = (1, 2, 3, 4)
  print d

  # 遍历
  for x in tup:
    print x
  for x, y in enumerate(tup):
    print x
    print y
  print '~~~~~~'

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
  # tup.append(5)
  #  tup [0] = '5'
  #  del tup[1]
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


