#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1] #方括号
  # 切片
  print tup[2:3]
  # 是否存在某值
  print tup[1 in tup]
  # 赋值
  a,b,c,d=[1,2,3,4] 
  print a
  print b 
  # 遍历
  for item in tup: #别忘了冒号
    print item
  for index, item in enumerate(tup):
    print index

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(2)
    #del tup[2]
    #tup[0]='qqq'
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


