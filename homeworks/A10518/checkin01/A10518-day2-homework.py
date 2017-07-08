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
  
  #03. try to explain what's float 数据类型
  print 'pie cost %d ' % (pie_total_price) # 格式化输出，这里输出结果是“pie cost 40”
  print 'pie cost %g ' % (pie_total_price) #输出结果是“pie cost 40.2” 取小数
  print 'pie cost %0.2f ' % (pie_total_price) #保留两位小数

  #04. 
  number = 2**3 
  print 'number = %d' % (number) #输出2的3次方

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ (没懂什么叫取模和按位)
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2) #简明教程里说这里应该回TRUE
  print 'test: %d' % (1 >= 2) #FALSE
  if 1:
    print 'goog'
  if 0:
    print 'xxx'

  if(2 != 2):
    print 'wweewe we w'
  #请开始你的表演


if __name__ == '__main__':
  main()