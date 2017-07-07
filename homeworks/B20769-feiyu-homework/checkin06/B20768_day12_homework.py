#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu

def main():
  tup = (1,2,4,8)#定义一个元组，此处用小括号（），而非[]

  #取值
  print tup[1]#取小标为1的元素，实际为第2个元素，此处为方括号[]
  # 切片
  print tup#输出整个元组
  print tup[0:3]#输出下标为0,1,2,3的元素
  print tup[2:]#从下标为2的元素开始，输出所有元素

  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
  # 赋值
  a,b,c,d = tup  #等同于a,b,c,d = (1,2,4,8)
  print a
  print b
  print c
  print d
  # 遍历
  for item in tup:#遍历元组tup中的所有元素
    print item

  for index,item in enumerate(tup):#遍历元组tup中的所有下标和对应元素
    print index  
    print item

  print '-------------'
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  
  #tup[4] = 16 #TypeError: 'tuple' object does not support item assignment
  #tup[3] = 16 #TypeError: 'tuple' object does not support item assignment
  #del tup[3]  #TypeError: 'tuple' object does not support item assignment

  try:
    pass
  except Exception, e:
    print e

if __name__ == '__main__':
  main()


