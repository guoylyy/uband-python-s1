#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
def talk_with_dad(is_cheap3, buy_amount3, good_description3):
  

   if is_cheap3:
    print "When she came back home, she told dad that she bought %d/kg %s for the cheap price." % (buy_amount3, good_description3)
    is_cheap3 = True

   else:
    print"She came back home and told dad that she bought nothing because the %s price was beyond their budget." % (good_description3)
    is_cheap3 = False

def acount(who3, is_cheap3, good_price3, buy_amount3):
  fee = good_price3 * buy_amount3
  if is_cheap3:
   print "Later that day, %s recorded %d yuan's expense on the book." % (who3, fee)
   is_cheap3 = True

def buy():
  good_price = 4
  reasonable_price = 5
  buy_amount = 2 
  who = 'Mom'
  good_description = 'cabbages'
  is_cheap = False

  print '%s saw %s sold at %d/kg on the steet.' % (who, good_description, good_price)
  if good_price <= reasonable_price:
    print "She thought that's cheap."
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
     buy_amount = 4
    print '"Why not buying %d kilograms?" she thought.' % (buy_amount)
  else:
    print "She thought that's expensive."
    is_cheap = False
    print 'So she left without buying a thing.'

  return who, is_cheap, good_price, buy_amount, good_description

def main():
  who2, is_cheap2, good_price2, buy_amount2, good_description2 = buy()
  talk_with_dad(is_cheap2, buy_amount2, good_description2)
  acount(who2, is_cheap2, good_price2, buy_amount2)

if __name__ == '__main__':
  main()
  

