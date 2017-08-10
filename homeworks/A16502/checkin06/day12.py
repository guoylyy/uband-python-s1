#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小仙女

def main():
  tup = (1,2,3,4)

  #取值
  print tup[0]#[]中是上标
  print tup[1]
  # 切片
  print tup
  print tup[0:3]#同list一样左闭右开
  print tup[2:]#右边没有意味着到最后
  
  # 是否存在某值
  print(1 in tup)
  print(9 in tup)
  # 赋值
  a,b,c,d=(1,2,3,4)
  print b
  # 遍历
  for item in tup:
    print item
  for index, item in enumerate(tup):
    print index

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(5)#不成功
    del tup[4]#不成功
    tup[2]=6
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


