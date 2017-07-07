#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

def main():
  tup = (1,2,3,4)

  #取值
  print tup[2]
  # 切片
  print tup[1:4]
  # 是否存在某值
  print (2 in tup)
  print (5 in tup)
  # 赋值
  a,s,d,f=(1,2,3,4)
  print a
  print s
  print d
  print f
  # 遍历
  print '遍历-------'
  for item in tup:
    print item
  print '-----------'  
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #1.插入
    #tup.append(5)
    #2.修改
    #tup [2]='two'
    #3.删除
    del tup[2]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


