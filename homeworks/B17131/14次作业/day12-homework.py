#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

#列表就像我们日常排队买奶茶或者肉夹馍的队伍(不稳定,既可以插入又可以删除又可以修改)。
#而元祖，它实际上像一个军队的队伍(相对稳定的，无插队，无删除，无修改)
#tuple 

def main():
  #      0 1 2 3   #因为index默认为0嘛
  tup = (1,2,3,4) #*用小括号来定义

  #取值
  print tup[1] #2
  # 切片
  print tup #(1,2,3,4)
  print tup[0:3]#(1,2,3)
  print tup[2:]#(3,4)
  
  # 是否存在某值
  print(1 in tup) #True
  print(5 in tup) #False
  
  # 赋值
  a,b,c,d= tup # a,b,c,d = (1,2,3,4)
  print a #1
  print b #2
  print c #3
  print d #4
  
  print '-----'
  # 遍历
  for item in tup:
    print item #1
               #2
               #3
               #4

  print 'enumerate-------'
  for index, item in enumerate(tup):
    print index
    print item
    #出来效果：    #0----index
                  #1----item
                  #1----index
                  #2----item
                  #2....
                  #3
                  #3
                  #4


  
  print "-------"               
  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    #tup.append(9)  #插入失败
    #del tup[0]     #删除失败
    #tup[0]='aaa'   #修改失败 
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


