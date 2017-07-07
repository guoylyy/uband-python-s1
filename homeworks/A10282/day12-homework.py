#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 233

def main():
  tup = (1,2,3,4)

  #取值
  print tup [0]
  print tup [3]
  print '-------------'
  # 切片
  print tup [0:2]
  print tup [1:4]
  print '-------------'
  # 是否存在某值
  print (3 in tup)
  print (6 in tup)
  print '-------------'
  # 赋值
  a, b, c, d = tup
  a, b, c, d = (1, 2, 3, 4)
  print a
  print c
  print '-------------'
  # 遍历
  for index, item in enumerate(tup):
    print item
    print index
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(8)
    tup[2] = aaa
    del tup
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()