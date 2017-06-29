#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yikuai

def main():
  tup = (1,2,3,4)

  #取值
  print '----quzhi------'
  print tup[1]
  # 切片
  print '----qiepian-----'
  print tup
  print tup[1:3]
  print tup[2:]
  # 是否存在某值
  print '----panduan------'
  print (1 in tup)
  print (4 in tup)
  print (5 in tup)
  # 赋值
  print '---fuzhi------'
  a,b,c,d = tup
  print a
  print b
  print c
  print d
  # 遍历
  print '----bianli-one----'
  for item in tup:
    print item 

  print '----bianli-two----'
  for item in tup[1:3]:
    print item

  print '----bianli-three---'
  for index,item in enumerate(tup):
    print index
    print item

  print '----try-------'
  # 花式报错
  # 不支持 1)插入 2)删除 3) 修改
  try:
    # tup.append(8)    #'tuple' object has no attribute 'append'
    # del tup[2]       #'tuple' object doesn't support item deletion
    # tup[0] = 'ace'   #'tuple' object does not support item assignment
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()
