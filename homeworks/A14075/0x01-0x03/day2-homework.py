#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: hydewww

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
  print ('pie cost %d ' % (pie_total_price))
  print ('pie cost %g ' % (pie_total_price))
  print ('pie cost %0.2f ' % (pie_total_price))

  #04. **
  number = 2**3
  print ('number = %d' % (number))

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print ('test: %d' % (1 != 2))
  print ('test: %d' % (1 >= 2))
  if 1:
    print ('goog')
  if 0:
    print ('xxx')

  if(2 != 2):
    print ('wweewe we w')
  #请开始你的表演
  
#---test begin.
  
  a = 2
  b = 3
  # 加减乘 乘方
  print (a+b,a-b,a*b,a**b)
  # 除分浮点除和整除+取余
  print (a/b,a//b,a%b)
  # 位运算(二进制) 与 或 异或 主要用在信号计算或神秘的acm/密码学
  # 印象中也可以用来做进制转换
  print (a&b,a|b,a^b)
  # 没听说过的按位翻转 ~ 看起来应该是原码补码的问题 
  print (~a)
  # 比较符 结果为True/False
  print (a>b)
  print (a<=b)
  # 逻辑符 True False要大写
  t = True
  f = False
  print (a>=b or t)
  print (a<b and f)
  
#---test over
  
if __name__ == '__main__':
  main()