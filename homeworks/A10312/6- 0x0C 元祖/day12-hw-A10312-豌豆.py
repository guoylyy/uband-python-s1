#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou

def main():
  tup = (1,2,3,4)

  #取值
  print '---取值 '
  print tup[2]
  
  # 切片
  print '---切片 '
  print tup
  print tup[0:3]
  print tup[1:]
  # 是否存在某值
  print '---存在与否 '
  print (3 in tup)
  print (6 in tup)
  # 赋值
  print '---赋值 '
  q,w,e,r = tup
  print q
  print w
  print e
  print r
  
  # 遍历
  print '---遍历 '
  for item in tup:
    print item

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


