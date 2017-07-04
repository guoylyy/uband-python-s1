#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

# 元组/数组定义和运算  tuple
# 元组不支持 插入，修改，删除操作。

def main():
  tup = (1,2,3,4)
  tup1 = ('one','two','three','four')

  #取值
  print (tup[0])
  print (tup1[0])

  # 切片
  print (tup)
  print (tup1)
  print (tup[0:2])
  print (tup1[1:])
  
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
  print ('onee' in tup1)
  print ('-------')
  
  # 运算
  print (tup * 2)
  print (tup + tup1)
  print (tup[2],tup1[1])
  print (tup1[2] + tup1[1])
  print (tup[1]+tup[2])

  # 赋值
  a,b,c,d = tup
  print (a,b,c,d )

  a,b,c,d = ('one','two','three','four')
  print (a,b,c,d)
  print ('_______')
  # 遍历
  for it in tup:
    print (it)
  for index,item in enumerate(tup):
    print(index,item)
  
  # 花式报错  不支持 1)插入 2)修改 3) 删除
  # tup.append(5) # 插入失败 'tuple' object has no attribute 'append'
  # del tup[3]  #删除失败 'tuple' object doesn't support item deletion
  # tup[0] = 'aa' #修改失败 'tuple' object does not support item assignment
  
if __name__ == '__main__':
  main()


