#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin

def main():
  tup = (1,2,3,4)     # tup用的是圆括号()  lst是方括号[]   字典用的是花括号{}
#        0 1 2 3
  #取值
  print tup[1]    #取1号值
  # 切片
  print tup
  print tup[0:3]   #一定要注意用的是冒号
  print tup[2:]    #取到最后一个值  如果后面写2:3 反而会跳出来（3，） 
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)

  # 赋值
  a,b,c,d = tup     #相当于把tup里面的1,2,3,4 赋值给了abcd
  print a 
  print b
  print c
  print d
  # 遍历
  print ' for --------'
  for item in tup:
  	print item

  print ' enumerate --------'
  for index, item in enumerate(tup):
  	print index

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(9)  # 插入失败   'tuple' object has no attribute 'append'
    #tup[0] = 'aaaa' # 修改失败  'tuple' object does not support item assignment
    del tup[0]    #删除失败  'tuple' object doesn't support item deletion
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


