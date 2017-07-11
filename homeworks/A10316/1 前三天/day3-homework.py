#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin


# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
     #答：一组代码只解决一个问题。多个动作的时候，就再重新来个def。

# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

def record_account(is_cheap2, good_price2, buy_amount3):
  if is_cheap2:
    record_account = good_price2 * buy_amount3

    print '妈妈回家拿出记账本，写下今天花了%d钱' % (record_account)


def talk_to_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了%d斤”' % (buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'
	
def buybuybuy():
  good_price = 3   #是一个会变的数字，每降低1元，多买1斤
  reasonable_price = 5
  buy_amount = 2   #是一个会变的数字，每降低1元，多买1斤

  who = '三连音的妈妈'
  good_description = '西双版纳大白菜'

  is_cheap = False

  print '%s上街看到了 %s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:    # 这种结尾的冒号要特别注意，如果丢了的话要补上
    print '她认为很便宜'
    is_cheap = True

    #开始考虑买几斤的问题    5-2  4-3 3-4 2-4   最多买四斤
    buy_amount = 2 + (reasonable_price - good_price)

    if buy_amount > 4:
      buy_amount = 4

    print '她买了 %d 斤' % (buy_amount)
  else:
  	print '她认为贵了'
  	is_cheap = False
  	print '她并没有买，扬长而去'

  return is_cheap, buy_amount, good_price

def main():
  #买
  is_cheap2, buy_amount2,good_price2 = buybuybuy()
  #说
  talk_to_daddy(is_cheap2, buy_amount2)
  #记账
  record_account(is_cheap2, good_price2, buy_amount2)

if __name__ == '__main__':
  main()