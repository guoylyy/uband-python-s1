#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[3]
  # 切片
  print tup [1:3]
  # 是否存在某值
  print tup[0]==1
  print 2 in tup
  # 赋值
  e,f,g,h = tup
  print f
  # 遍历
  #for index, item in tup:
  for index, item in enumerate (tup):
    print '%d, %d' % (index, item)

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(5)
    #tup[2]=1
    del tup[2]

  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


