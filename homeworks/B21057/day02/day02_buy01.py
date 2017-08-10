#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: fangcheng
 
# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2
 
def main():
  #01.int 
  apple_price = 5
  banana_price = 6
  watermelon_price = 4.5
  apple_mount = 4
  banana_mount = 8
  watermelon_mount =10
   
  #02. *  /
  apple_total_price = apple_mount * apple_price
  banana_total_price = banana_mount * banana_price
  watermelon_total_price = watermelon_mount * watermelon_price
  print ' 小明买了 %d 元苹果' %(apple_total_price)
  print ' 小强买了 %d 元香蕉' %(banana_total_price)
  print ' 小芳买了 %d 元西瓜' %(watermelon_total_price)
   
  #03. try to explain what's float
  #浮点数是数学中带有小数点的数
 
  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  xiaoming_data = 6
  xiaoqiang_data = 3
  if xiaoqiang_data < xiaoming_data:
    print '小强摇骰子赢了小明'
  else:
    print '小明摇骰子赢了小强'

  #请开始你的表演
 
if __name__ == '__main__':
  main()
