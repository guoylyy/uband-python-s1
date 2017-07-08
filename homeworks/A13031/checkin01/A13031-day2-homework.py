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
  #6.//
  number1 = 10//3
  print 'number1 = %d' % (number1)
  #7.%
  number2 = 10%3
  print 'number2 = %d' % (number2)
  #8.<<
  number3 = 10<<3
  print 'number3 = %d' % (number3)
  #9.>>
  number4 = 10>>3
  print 'number4 = %d' % (number4)
  #10.&
  number5 = 10&3
  print 'number5 = %d' % (number5)
  #11.|
  number6 = 10|3
  print 'number6 = %d' % (number6)
  #12.^
  number7 = 10^3
  print 'number7 = %d' % (number7)
  #13.<
  number8 = 10<3
  print 'number8 = %d' % (number8)
  #14.>
  number9 = 10>3
  print 'number9 = %d' % (number9)
  #15.not
  number10 = not 10<3
  print 'number10 = %d' % (number10)
  #16.and
  number11 = 10>3  and 10<3
  print 'number11 = %d' % (number11)
  #17.or
  number12 = 10>3  or 10<3
  print 'number12 = %d' % (number12)
  print 'What is float? '
  print "float是一种数据类型 "
  print "表示单精度浮点数，精度为7位 "
  

if __name__ == '__main__':
  main()