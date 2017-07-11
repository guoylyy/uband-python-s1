#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: hydewww

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
#
# # 3天作业打卡方式
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
#

# 单一职责 每个函数只做一件事?

def record_account(buy_amount4,good_price4):
    print("Record: I've paid %d yuan today." %(buy_amount4*good_price4))

def buybuybuy():
  good_price = 3
  reasonable_price = 5
  buy_amount = 2

  who = 'Mom'
  good_description = "Nice Cabbage"

  is_cheap = False

  print ('%s saw "%s" sold at %d yuan per catty when shopping. ' % (who, good_description, good_price)  )

  if good_price <= reasonable_price:
    print ('She thought it was cheap.')
    is_cheap = True

    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print ('She bought %d catty' % (buy_amount) )
  else:
    print ('She thought it was expensive. ')
    is_cheap = False
    print ("She didn't buy it. ")

  return is_cheap, buy_amount, good_price

def talk_with_daddy(is_cheap3,buy_amount3):
    if (is_cheap3):
        print ("Mom said to Daddy: Today's vegetable is cheap.I've bought %d catty." %buy_amount3)
    else:
        print ("Mom said to Daddy: Today's vegetable is expensive.")


def main():
  #买买买
  is_cheap2, buy_amount2 , good_price2 = buybuybuy()
  #说说说
  talk_with_daddy(is_cheap2, buy_amount2)
  #记记记
  record_account(buy_amount2,good_price2)

if __name__ == '__main__':
  main()
