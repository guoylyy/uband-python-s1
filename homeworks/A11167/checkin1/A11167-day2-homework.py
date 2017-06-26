#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Betty


def main():
  #01.int 整数
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7
  
  #02. *  / 乘除
  apple_total_price = apple_number * apple_price
  pie_total_price = pie_number * pie_price
  
  #03. try to explain what's float
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %g ' % (pie_total_price)
  print 'pie cost %0.2f ' % (pie_total_price)
  #float就是带小数点的数，而且这个小数点是可以浮动的。

  #04. ** 幂
  number = 2**3 #2的三次方
  print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2)
  print 'test: %d' % (1 >= 2)
  if 1:
    print 'goog'
  if 0:
    print 'xxx'

  if(2 != 2):
    print 'wweewe we w'
  #请开始你的表演

  #+ - 加减
  total_number = apple_number + pie_number
  price_con = apple_price - pie_price
  
  print 'total number %d ' % (total_number)
  print 'a pie costs %0.2f more than an apple' % (price_con)
  
  #// 取整除，返回商的整数部分
  x = pie_price // apple_number
  print x

  # & | 按位与，按位或：二进制
  a = apple_number & pie_number
  b = apple_number | pie_number
  print a
  print b
  
 

if __name__ == '__main__':
  main()