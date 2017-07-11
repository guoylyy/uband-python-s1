#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania
#元组tuple：无插队，无删除，无修改 （相对稳定）
#列表list：可插队，可删除，可修改（相对不稳定）

def main():
  tup = (1,2,3,4)

  #取值
  print tup[3]

  # 切片
  print '-----'
  print tup
  print tup[0:3]
  print tup[2:]
  
  # 是否存在某值
  print '-----'
  print (1 in tup)
  print (5 in tup)
  
  # 赋值
  print '-----'
  a,b,c,d = (1,2,3,4) #元组的特性
  print a
  print b
  print c
  print d
  
  # 遍历
  print '-----'
  for item in tup:
    print item
  
  print '---enumerate---'  
  for index, item in enumerate(tup):
    print index


  print '-----'
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(9) #插入失败 'tuple' object has no attribute 'append'
    del tup[0]    #删除失败 'tuple' object doesn't support item deletion
    tup[0] = 'aaa'  #修改失败 'tuple' object does not support item assignment
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


