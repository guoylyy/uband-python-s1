#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
#      我认为这指的是一个函数下定义的某变量应该只在这一函数下起作用，不会影响其他函数
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
#      好感动嘤嘤嘤！本来啥也不会的英专狗，照着蜀黍的视频和sample code居然把记账函数写出来了！我爱debug！！！
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡


#今天买了xxx，花了xxx元
def record_account(is_cheap4, buy_amount4, good_price2):
  value = buy_amount4 * good_price2
  if is_cheap4:
  	print '老妈在小本子上记了买菜花销 %d 元' % (value)
  else:
  	print '今天没有买菜'

#注意：记账应该记的是菜品名称，以及具体价钱。若没有开销，则无需记账，记账过程的函数可以pass
 # if value > 0:
 #   print '老妈记账: 今天买了 %s , 花费了 %d 元' % （good_name, cost）
 # else:
 #   pass


def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
	print '老妈回到家里，跟老爸说："今天去买菜，价格不贵，买了 %d 斤"。' % (buy_amount3)
  else:
  	print '老妈回到家里，跟老爸说："今天去买菜，菜好贵啊，没买"。'


def buy_buy_buy():
  who = "Pennsylvania的老妈"
  good_description = "西双版纳大白菜"

  good_price = 3
  reasonable_price = 5
  buy_amount = 2
  

  is_cheap = False

  print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount) 
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'


  return is_cheap, buy_amount, good_price



 
def main():
  #买买买
  is_cheap2, buy_amount2, good_price = buy_buy_buy()
  #说说说
  talk_with_daddy(is_cheap2, buy_amount2)  
  #记记记
  record_account(is_cheap2, buy_amount2, good_price)

if __name__ == '__main__':
  main()