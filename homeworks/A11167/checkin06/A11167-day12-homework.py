#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: bettyyan

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print '---'
  print tup
  print tup[0:3]
  print tup[2:]
  # 是否存在某值
  print '---'
  print (1 in tup)
  print (5 in tup)
  # 赋值
  print '---'
  a,b,c,d = (1,2,3,4)
  print a
  print b
  print c
  print d
  # 遍历
  print '---'
  for item in tup:
  	print item

  for index, item in enumerate(tup):
  	print index

  # 花式报错
  print '---'
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(9) #插入
    del tup[0] #删除失败
    tup[0] = 'aaa' #修改失败
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


