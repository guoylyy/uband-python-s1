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
  print 'pie cost %d ' % (pie_total_price)  # %d 表示整数
  print 'pie cost %g ' % (pie_total_price)  # %g 显示出整数部分以及分数部分
  print 'pie cost %0.2f ' % (pie_total_price) #%0.2f 表示保留小数点后两位，采用四舍五进

  #04. **
  number = 2**3 # **表示幂
  print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2) # !=不等于
  print 'test: %d' % (1 >= 2) #1>= 大于等于
  if 1:
    print 'goog' # 问题，为什么if语句中最后打印出来的是‘goog’
  if 0:
    print 'xxx'

  if(2 != 2):
    print 'wweewe we w'
  #请开始你的表演
  number1=3+3
  print number1
  number2=3-3
  print number2
  number3=3*3
  print number3
  number4 = 3**3
  print number4
  number5 = 6/4
  print number5
  number6=6//4
  print number6
  print '_____'
  number7=6%4
  print number7
  number8=6&4 # &按位与 不懂
  print number8
  number9=6|4 #|按位或 不懂
  print number9
  number10 =6^4 # 按位异或 不懂
  print number10
  number11= True
  number12=False
  print not number11 
  print number11 and number12
  print number11 or number12



if __name__ == '__main__':
  main()

