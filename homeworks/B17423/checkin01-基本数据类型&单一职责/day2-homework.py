#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

# homework2

def main():
  #01.int 
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7
  
  #02. *  /
  apple_total_price = apple_number * apple_price  #24
  pie_total_price = pie_number * pie_price   #40.2
  
  #03. try to explain what's float
  print ('pie cost %d ' % (pie_total_price))  #40
  print ('pie cost %g ' % (pie_total_price))  #40.2  根据数值的不同自动选择%e或%f
  print ('pie cost %0.2f ' % (pie_total_price)) #40.20 浮点数，小数点后两位

  #04. **
  number = 2**3   #2^3=8
  print ('number = %d' % (number))   #8

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print ('test: %d' % (1 != 2))  #1!=2,return 1
  print ('test: %d' % (1 >= 2))  #1<2, return 0
  if 1:         #1=true,print
    print ('goog')
  if 0:          #0=false,不执行
    print ('xxx')

  if(2 != 2):
    print ('wweewe we w')
  #请开始你的表演
  print ('%d+%d=%d' % (3,5,3+5))
  print ('%d-%d=%d' % (50,24,50-24))
  print('a+b=ab:')
  print ('a'+'b')  #ab
  print (4/3)  #1.3333
  print (4//3.0) #1商
  print (4%3)  #1余数
  print (2<<2) #8: 0010--1000
  print(11>>1) #5::1011--0101
  print(5&3) #1: 0101 & 0011 = 0001按位与
  print(5|3) #7: 0101 | 0011 = 0111按位或
  print(5^3) #6: 0101 ^ 0011 = 0110按位异或
  print(~5)  #6: ~0101 = -(x+1) 按位翻转
  print(5<3) #False
  print(5>3) #True
  print(5==3) #False
  print(5!=3) #True
  print(not(1==2)) #not false = ture
  print((1>2) and (2<3)) #false and true = false
  print((1>2) or (2<3)) #false or true = true

if __name__ == '__main__':
  main()