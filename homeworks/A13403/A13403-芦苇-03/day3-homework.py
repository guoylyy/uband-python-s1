#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: luwei

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
 

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下

# day1 加分题
def main():
  good_price = 6  #每降低一元。多买一斤
  reasonable_price = 5
  buy_amount = 2  #每降低一元。多买一斤
  
  who = 'luwei的老妈'
  good_description = "西双版纳大白菜" 

  is_cheap = False 
  

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4 
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
    	buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()

print '-----------------------'
# 今天的sample
# 1.function (code block)
# 	one file multiple function (code block)
# 2.return (pass variable)
# 3.return multiple variable
#
##原则#单一职责原则
#

def talk_with_daddy(is_cheap3,buy_amount3):
	
	if is_cheap3:
		print '老妈回到家里，跟老爸说："今天去买菜，价格不贵，买了 %d 斤"。 ' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵额，没买"。'

def buybuybuy():
  good_price = 6  #每降低一元。多买一斤
  reasonable_price = 5
  buy_amount = 2  #每降低一元。多买一斤
  
  who = 'luwei的老妈'
  good_description = "西双版纳大白菜" 

  is_cheap = False 
  

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4 
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
    	buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

  return is_cheap,buy_amount


def main():
  #买买买
  is_cheap2,buy_amount2 = buybuybuy()
  #说说说
  talk_with_daddy(is_cheap2,buy_amount2)

 
if __name__ == '__main__':
  main()
	

print '-----------------------'




# 2. 解释一遍自己眼中的单一职责原则是什么？
# 一个代码块只做一件事情
# 一个类应该只有一个发生变化的原因 一个代码块应该有且只有一个改变的原因







# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）

def record_account(is_cheap, good_description,buy_amount, good_price):

  if is_cheap:
    total_price = buy_amount * good_price
    print  '老妈在小本子记了“买了 %d 斤 %s ,花销 %d 元。” ' %(buy_amount,good_description,total_price)

def talk_with_daddy(is_cheap,buy_amount):
  
  if is_cheap:
    print '老妈回到家里，跟老爸说："今天去买菜，价格不贵，买了 %d 斤"。 ' %(buy_amount)
  else:
    print '老妈回到家里，跟老爸说："今天去买菜，菜好贵额，没买"。'

def buybuybuy():
  good_price = 3  #每降低一元。多买一斤
  reasonable_price = 5
  buy_amount = 2  #每降低一元。多买一斤
  
  who = 'luwei的老妈'
  good_description = "西双版纳大白菜" 

  is_cheap = False 
  

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4 
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

  return is_cheap,good_description,buy_amount,good_price


def main():
  #买买买
  is_cheap,good_description,buy_amount,good_price = buybuybuy()
  #说说说
  talk_with_daddy(is_cheap,buy_amount)
  #记记记
  record_account(is_cheap,good_description,buy_amount,good_price)

 
if __name__ == '__main__':
  main()