#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu


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
  

  print 'test: %d' % (9 + 2 + 5)
  print 'test: %d' % (8 - 2 - 7)
  print 'test: %d' % (6 * 6)
  print 'test: %d' % (5 ** 4)
  print 'test: %g' % (13 / 4.0)
  print 'test: %g' % (13 // 4.0)

  number = 8 % 3
  print 'number = %d' % (number)
  number = 5 & 3
  print 'number = %d' % (number)
  number = 5 | 3
  print 'number = %d' % (number)
  
  print 'test: %d' % (1 < 0)
  if 1:
    print 'oui'
  if 0:
    print 'non'
  if(3 > 2):
    print 'apprendre'
  
  print 'test: %d' % (5 >= 3)
  if 1:
    print 'bonjour'
  if(4 <= 3):
    print 'comprendre'
    

  print 'test: %d' % (3 == 4)
  if(6 != 5):
    print 'bonsoir'
  if(8 != 8):
    print 'faire'

  a = 2 > 1
  b = 2 < 1
 
  if not a:
    print 'a项错'
  if not b:
    print 'b项对'

  if a and b:
    print 'la'
  else:
    print 'le'

  if a or b:
    print 'du'
  else:
    print 'au'

if __name__ == '__main__':
  main()