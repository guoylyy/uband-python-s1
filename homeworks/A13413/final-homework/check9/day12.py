#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: joylin
def main():
  tup = (5,6,7,8)
 
  #取值
  print tup[1]
  # 切片
  print tup[1:4]
  # 是否存在某值
  print (1 in tup)
  # 赋值
  a,b,c,d = (5,6,7,8) 
  print b
  print d 
  print "-----"
  # 遍历
  for item in tup:
    print item
  print "-----"
  for index, item in enumerate(tup):
    print index
    print item
  print '-----'
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(7)
    #del tup[2]
    tup[0] = 'aaa'  #修改失败
  except Exception, e:
    print e
   
if __name__ == '__main__':
  main()