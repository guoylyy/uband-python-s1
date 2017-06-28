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
  peach_price=8.9
  peach_number=7.5
  pear_price=9
  pear_number=20

  peach_total_price=peach_number*peach_price
  pear_total_price=pear_number*pear_price

  print "peach_cost %d " % (peach_total_price)
  print "peach_cost %g "%(pear_total_price)
  print "peach_cost %0.2f"% (pear_total_price)

  print "pear_cost %d"% (pear_total_price)
  print "pear_cost %g"% (pear_total_price)
  print "pear_cost %0.2f"%(pear_total_price)


  number=3**5
  print "numbe= %d"%(number)




  if (3!=2):
  	print "why do you care"


if __name__ == '__main__':
  main()