#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Casey

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[0:3]
  print tup[2:]

  # 是否存在某值
  print {1 in tup}
  print {6 in tup}

  
  # 赋值
  a,b,c,d = tup
  print a
  print b
  print c
  print d
  print '------------'
  # 遍历
  for item in tup:
    print item
  print '-----------'

  for index, item in enumerate(tup):
    print index
    #print item

  # 花式报错

  # 不支持 1)插入 2)修改 3) 删除
  try:
      #tup.append(7)  #插入 
      #del tup[0]  #删除
      tup[0] = 'bb'  #修改


  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


