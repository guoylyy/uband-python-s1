#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: suancaiyu
#学习内容：
#1,练习python中运算符，和表达式 单个字符或数值可以构成表达式吗？
#2,print 语句输出格式化 %0.2f 


def main():
  apple_numbe = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.782

  apple_total_price = apple_numbe * apple_price
  pie_total_price = pie_number * pie_price

  print 'pie cost %d' % (pie_total_price)     #pie的总价格 到整数
  print 'pie cost %g' % (pie_total_price)     #保留小数点  
  print 'pie cost %0.2f' % (pie_total_price)  #保留小数点后两位   由f前的数字决定保留几位

  number = 2**3     #  ** 次方
  print 'number = %d' % (number)

  print 'test: %d' % (1 != 2)          #!=不等于
  print 'test: %d' % (1 >= 2)

  if 1:
    print 'goog'        #不太清楚这边的if正确，是哪里正确了
  if 0:
    print 'xxx'

  if(2 != 2):          
    print 'hello,world'
	
	
#p34的练习

  #简单的加减乘除之类的
  number = 2+3                     #必须要缩进，不然会被忽视
  print 'number = %d' %(number)    #打完上面一行，得print才会在下面框框显示
  
  number = 10%3                    #//取商，即3； %取余数，即1.
  print 'number = %d' %(number)

  #比较
  x = 'star'
  y = 'stAr'                       #定义x，y 的时候，如果是字符，一定要加引号

  if (x == y):                     #等于的符号是：==
	print 'cool'

  if (x != y):
	print 'oh no'

  #and,or    not不会用
  x = True                          #这个地方可以打True、False，也可以打1,0
  y = 2**3
  number = x and y                 # x如果是False，and 返回False 否则返回y的值
             #or                   # x如果是True， or 返回Ture，否则返回y的值

  print 'number =%d' %(number)     #实在不知道这句话干嘛用的，但是好好用。先就用着吧



  #对比大小的一种方式，好原始。
  x = 5
  y = 6

  if x <= y:
	print 'True'
  else:
	print 'False'    

  #对比大小    不需要定义
  print '%d' %( 5 <= 6 )


if __name__ == '__main__':
  main()
