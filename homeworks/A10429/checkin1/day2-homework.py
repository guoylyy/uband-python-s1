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
# homework  practice  page34 所有运算符
def main():
  #01.int
  orange_number = 6
  orange_price = 3.7
  cake_number = 3
  cake_price = 4.6

  #02.* /
  orange_total_price = orange_number * orange_price
  cake_total_price = cake_number * cake_price

  #03. float
  print 'orange cost %d' % (orange_total_price)
  print 'orange cost %g' % (orange_total_price)
  print 'orange cost %0.2f' % (orange_total_price)

  #04. **
  number = 2**3
  print 'number = %d' % (number)

  #05. + - * /
  a = 2 + 3
  print '2+3=%d' % (a)
  a = 3 -2 
  print '3-2=%d' %(a)
  a = 2-3
  print '2-3=%d' %(a)
  a = 2 / 2
  print '2/2=%d' %(a)
  a = 0.2 / 2
  print '0.2/2=%g' %(a)
  a = 3.0/4
  print '3.0/4=%g' %(a)

  #06.// %
  b = 4 // 3.0
  print '4//3.0=%g' %(b)
  b = -25.5%2.25
  print  b # '-25.5%2.25=%g' %(b)?

  #07.<< >>
  c = 2<<2
  print '2<<2=%d' %(c)
  c = 11>>1
  print '11>>1=%d' %(c)

  #08. & | ^ ~
  d = 5 & 3
  print '5&3=%d' %(d)
  d = 5 | 3
  print d
  d = 5 ^ 3
  print d
  d = ~5
  print d

  #09. < > <= >= == !=
  print 'compare: %d' % (1<2)
  print 'compare: %d' % (2>3)
  print 'compare: %d' % (1<=2)
  print 'compare: %d' % (1>=2)
  x = 2
  print 'compare: %d' % (2==x)
  y = 5.0
  z = 3
  print 'compare: %d' % (y==z)
  print 'combine: %f' % (x+(y/z))

  if 5 != 2:
   print 'right'
  else:
   print 'wrong'

  if 'nageshui':
    print 'nageshui'
  if 0:
    print 'false'
  if 1:
    print 'true'

  #10. not and or
  print ('w' and 'm')
  print (not 'w')
  print ('w' or 'm')
  print 'w' or 'm'
if __name__ == '__main__':
  main()


if __name__ == '__main__':
  main()