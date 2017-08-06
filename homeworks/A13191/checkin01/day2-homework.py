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

  var1 = 1
  var2 = 2
  var3 = 3
  var4 = 4

  var5 = var1 + var2
  var6 = var3 - var4
  var7 = var1 * var3
  var8 = var4 / var2
  var9 = var4 // var3
  var10 = 5
  var11 = var10 % var3

  print 'I am %d, %d, %d, %d, %d and %d, lol.' % (var5, var6, var7, var8, var9, var11)

  var12 = var9 << 1
  var13 = var10 >> 3
  var14 = 1 & 2
  var15 = 1 | 2
  var16 = 1 ^ 2
  var17 = ~ 2

  print 'I am %d, %d, %d, %d, %d and %d, hhhhhh.' % (var12, var13, var14, var15, var16, var17)

  if(2 < 3):
  	print "I love python."
  else:
  	print "I don't learn anymore."

  print "test a bunch of operators: %d, %d, %d, %d, %d" % (2 > 3, 2 <= 3, 2 >= 3, 2 == 3, 2 != 3)

  var18 = True
  var19 = False
  var20 = not var18
  var21 = var18 and var19
  var22 = var18 or var19
  print 'Ich bin %d, %d und %d, hahaha.' % (var20, var21, var22)

if __name__ == '__main__':
  main()