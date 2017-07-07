#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[2:4]
  print tup[1:]
  
  # 是否存在某值
  print (1 in tup)
  print (10086 in tup)
  
  # 赋值  ##即集体赋值
  a, b, c, d = tup #即 a, b, c, d = (1, 2, 3, 4)
  print a
  print b
  print c
  print d
  # 也适用于列表
  lst = [5, 6, 7, 8]
  q, w, e, r = lst
  print q, w, e, r

  # 遍历
  print '# 遍历'
  for tup_item in tup:
    print tup_item

  print 'enumerate'
  for tup_item, index in enumerate(tup):   #for a, b in enumerate(xx):  a默认为序数, b默认为item
    print index                            #for a in enumerat(xx):  a默认为(序数, item)
    print tup_item
  

  print 'try&except'
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(7) ## 1)'tuple' object has no attribute 'append': tup无法插入
    # tup[0] = 2  ##2)'tuple' object does not support item assignment: tup无法修改
    # del tup[0]  ##3)'tuple' object doesn't support item deletion: tup无法删除


  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


