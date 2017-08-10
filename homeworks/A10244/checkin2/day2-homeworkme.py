#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

def main():
  #01.int 
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7
  
  #02. *  /
  apple_total_price = apple_number * apple_price
  pie_total_price = pie_number * pie_price
  
  #03. try to explain what's float
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %g ' % (pie_total_price)
  print 'pie cost %0.2f ' % (pie_total_price)

  #04. **
  number = 2**3
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
  print 'test1: %s' % ('a' + 'b')
  print 'test2: %d' % (3 - 5)
  print 'test3: %s' % ('hello' * 4)
  print 'test4: %d' % (2 ** 4)
  print 'test5: %d' % (1.0 / 3)
  print 'test6: %0.2f' % (1.0 / 3)
  print 'test7: %0.3f' % (13 // 4)
  print 'test8: %d' % (13 // 4)
  print 'test9: %d' % (29 % 8)
  print 'test10: %d' % (7 << 1)
  print 'test11: %d' % (7 >> 1)
  print 'test12: %d' % (9 & 3)
  print 'test13: %d' % (5 | 3)
  print 'test14: %d' % (1 ^ 0)
  print 'test15: %d' % (~ 5)
  print 'test16: %d' % (7 < 5)
  if 1:
    print '%s' % ('true')
  if 0:
    print 'not%s' % ('true')


if __name__ == '__main__':
  main()