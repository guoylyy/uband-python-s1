#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

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
  #    每个符号在下面测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2)
  print 'test: %d' % (1 >= 2)
  if 1:
    print 'goog'
  if 0:
    print 'xxx'

  if(2 != 3):
    print 'wweewe we w'
  #请开始你的表演

  print "total number = %d " % (apple_number + pie_number)
  print "surplus number = %d " % (pie_number - apple_number)
  print "apple cost = %d " % (apple_total_price)
  number = 3**4
  print "number = %d " % (number)
  number1 = 8.0/3
  print "number1 = %g " % (number1)
  number2 = 8//3.0
  print "number2 = %0.2f " % (number2)
  number3 = 8%3
  print "number3 = %d " % (number3)
  

  if apple_number <= pie_number:
    print "True"

  if apple_price >= pie_price:
    print "no more apples"
  else:
    print "buy some apples"

  if(8 != 5):
    print "Different"





if __name__ == '__main__':
  main()