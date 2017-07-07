#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Janice YANG

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
  #01 + - * /
  apple_pie_price = apple_price + pie_price
  print 'apple pie price = %d' % (apple_pie_price)
  bias_total_cost = pie_price * pie_number - apple_price * apple_number
  print 'bias_total_cost = %d' % (bias_total_cost)
  
  #02 ** / // %
  a11 = 3**2   #9
  print 'all = %d' % (a11)
  a12 = 15/4   #3
  a13 = 15/4.0 #15.0/4
  print 'a12 = %d' % (a12)
  print 'a13 = %d' % (a13)
  a14 = 15/4.0
  print 'a14 = %d' %(a14)
  a15 = 15 % 4
  print 'a15 = %d' %(a15)

  #03 < > <= >= == !=
  weight = 57
  ideal_weight = 50
  crazy_weight = 60
  height = 163
  ideal_height = 167

  if weight <= ideal_weight:  #Tips:<=之间不要加空格
    print 'Eating and Eating'
  elif weight < crazy_weight:
    print 'Eating and Exercise'
  else:
    print 'No eating but exercise'
  if weight == ideal_weight:
    print 'hhhhh~~~'
  if height != ideal_height:
    print 'Exercise!'

  #04 not and or
  is_eating = False
  eat = True
  now_eat = not eat
  if now_eat == is_eating:
    print 'No eating'
  a41 = eat and now_eat #0
  print 'a41 = %d' %(a41)
  a42 =is_eating or eat #1
  print 'a42 = %d' %(a42)



if __name__ == '__main__':
  main()