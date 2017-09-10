#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[2]#记得这里要打中括号[]，和列表一样下标从0开始，不能同时取两个0，1，想要同时取多个值只能用切片
  # 切片
  print tup[0:1]#切片左边是闭区间，右边是开区间，即右边的实际取值会比写出来的下标少一位
  print tup[2:]#右边什么都不写，默认取到最后一位
  print tup[:3]#左边什么都不写，默认从第一位开始数
  # 是否存在某值
  print (1 in tup) #存在，则打印ture
  print (5 in tup) #不存在，则打印false
  if 1 in tup:
    a,b,c,d=(1,2,3,5) #可以利用元祖直接给多个变量赋值
    print a,b,c,d
  if not 5 in tup:
    a,b,c,d=(7,9,3,2)
    print a,b,c,d

  # 赋值
  x,y,z,q=tup
  print x+y,y+z,z+q
  
  # 遍历
  for item in tup:
    print item

  print "enumerate-------"

  for index,item in enumerate(tup):
    print index+item

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  print "---------"
  try:
    #tup.append(9)#插入失败
    #tup[2]=6#修改失败
    del tup[0] #删除失败

  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


