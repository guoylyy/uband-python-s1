#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

# Day2 - 运算符的运用
# homework2

def main():
  #01.int  
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7

  it = 'apple'
  
  #02. * 定义表达式 
  apple_total_price = apple_number * apple_price
  pie_total_price = pie_number * pie_price
  
  #03. try to explain what's float，变量赋值，并输出，说明各运算过程
  print ('pie cost %d ' % (pie_total_price))   # 把派总价取整数
  print ('pie cost %g ' % (pie_total_price))   # 把派总价取小数
  print ('pie cost %0.2f ' % (pie_total_price))  # 保留2位小数
  print ('pie cost %0.3f ' % (pie_total_price))  # 保留3位小数
  print ('pie and %s ' % (it))   #  字符串


  #04. **          幂运算
  number = 2**3
  print ('number = %d' % (number))

  #05. +-*/ // %
  jianfa = 4 - 2
  print ('number = %d' % (jianfa))

  jiafa  = 4 + 2
  print ('number = %d' % (jiafa))

  chengfa  = 4 * 2
  print ('number = %d' % (chengfa))

  chufa  = 4 / 2
  print ('number = %d' % (chufa))

  quzheng  = 9 // 2
  print ('number = %d' % (quzheng))

  qumo = 10 % 3
  print ('number qumo = %d' % (qumo))

  #06 else

  print ('test1: %d' % (1 != 2))
  print ('test2: %d' % (1 >= 2))
  print ('test3: %d' % (1 <= 2))
  print ('test4: %d' % (1 == 2))
  print ('test5: %d' % (1 < 2))

  print('________')
  a = 10; b = 20;c = 0;
  c = a + b
  print ('1-c值为：',c)
  c += a
  print ('2-c值为：',c)
 
  print (a and b) 
  print (a or b)

  print (not (a and b ))
  
  d = 0
  print (not (d and b ))
  print ('___d____')
  e=10
  print (a is e )


  if 1:
    print ('goog')
  if 0:
    print ('xxx')




if __name__ == '__main__':
  main()