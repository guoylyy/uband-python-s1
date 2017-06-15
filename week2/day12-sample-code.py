#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#今明两天完成的基础教程
#1. tuple
#2. try except
#完成后，我们周末做一个练习，然后下一周开始做实际的代码项目
def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[0:3]
  print tup[2:]
  
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
  
  # 赋值
  a,b,c,d = (1,2,3,4)
  print a
  print b
  print c
  print d
  
  print '---'
  # 遍历
  for item in tup:
    print item
  
  print ' enumerate---'  
  for index, item in enumerate(tup):
    print index


  print '---'
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    # tup.append(9) #插入失败
    # del tup[0]    #删除失败 'tuple' object doesn't support item deletion
    tup[0] = 'aaa'  #修改失败
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


