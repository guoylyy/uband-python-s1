#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi

def main():
  tup = (1,2,3,4)

  #取值
  print tup[2]
  # 切片
  print tup
  print tup[1:3]
  print tup[0:3] 
  print tup[1:]
  print tup[:1] 
  # 是否存在某值
  print (2 in tup)
  print (9 in tup)
  
  # 赋值
  o,p,q,r = tup
  print o
  print p
  print q
  print '~~~~~'
  # 遍历
  for item in tup:
  	print item

  print '~~~enumerte~~~~~'
  for index, item in enumerate(tup):
  	print '当前第%d' % (index)
  	print item

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(7) #'tuple' object has no attribute 'append'
    #tup[1] = '8' #'tuple' object does not support item assignment
    del tup[3]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


