#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

def main():
  # #01.int 
  # apple_number = 5
  # apple_price = 4.8
  # pie_number = 6
  # pie_price = 6.7
  
  # #02. *  /
  # apple_total_price = apple_number * apple_price
  # pie_total_price = pie_number * pie_price
  
  # #03. try to explain what's float
  # print 'pie cost %d ' % (pie_total_price)
  # print 'pie cost %g ' % (pie_total_price)
  # print 'pie cost %0.2f ' % (pie_total_price)

  # #04. **
  # number = 2**3
  # print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  
  my_money = 200000 #RMB
  shushu_money = 300000 #RMB
  total_money = my_money + shushu_money

  house_unit_price = 25000 #RMB/m^2
  house_space = 85 #m^2
  house_price = house_unit_price * house_space #总价
  house_amount = total_money // house_price #能买几套

  money_left = total_money % house_price #还剩多少钱


  if total_money >= house_price:
    if house_amount == 1:
      print "hooray, we can afford to buy an appartment! There is even an extra of ¥%0.1f left for the wedding" % (money_left)
    else: 
      print "hooray, we can afford to buy %d appartments! There is even an extra of ¥%0.1f left for the wedding" % (house_amount, money_left)
  else:
    money_short = house_price - total_money
    print "woops, we are ¥%d short" % money_short



if __name__ == '__main__':
  main()