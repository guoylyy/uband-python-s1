
# -*- coding: utf-8 -*-
# @author: shuan

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
def buy():
  
 who = '栓妈妈'
 good_price = 3
 good_description = '西双版纳大白菜'
 is_cheap = False
 reasonable_price = 5
 buy_amount = 2

 print"%s上街看到了%s卖%d元/斤"% (who, good_description, good_price)
 if good_price <= reasonable_price:                                        
  print'她认为便宜 '
  is_cheap= True
  buy_amount= 2 + (reasonable_price-good_price)
  if buy_amount > 4:
    buy_amount=4
  print'她买了%d斤 '%(buy_amount)
 else :
  print'她认为贵了 '
  is_cheap= False
  print'她并没有买，扬长而去 '
 return is_cheap,buy_amount
 
def talk(is_cheap,buy_amount):
	if is_cheap:
		print"今天去买菜，价格不贵，买了%d斤"%(buy_amount)
	else:
		print"今天去买菜，菜好贵啊，没买"

def main():
  is_cheap, buy_amount = buy()
  talk(is_cheap,buy_amount)

if __name__ == '__main__':
  main()


# 2. 解释一遍自己眼中的单一职责原则是什么？
#    一个代码块只能行使一个职责，但是不同代码块可以用return来交换信息
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
def buy():
  
 who = '栓妈妈'
 good_price = 3
 good_description = '西双版纳大白菜'
 is_cheap = False
 reasonable_price = 5
 buy_amount = 2

 print"%s上街看到了%s卖%d元/斤"% (who, good_description, good_price)
 if good_price <= reasonable_price:                                        
  print'她认为便宜 '
  is_cheap= True
  buy_amount= 2 + (reasonable_price-good_price)
  if buy_amount > 4:
    buy_amount=4
  print'她买了%d斤 '%(buy_amount)
 else :
  print'她认为贵了 '
  is_cheap= False
  print'她并没有买，扬长而去 '
 return is_cheap,buy_amount,good_price
 
def talk(is_cheap,buy_amount):
	if is_cheap:
		print"今天去买菜，价格不贵，买了%d斤"%(buy_amount)
	else:
		print"今天去买菜，菜好贵啊，没买"

def purchase_record(is_cheap,buy_amount,good_price):
    if is_cheap:
 	    print'老妈在小本子记了买菜花销%d元'%(buy_amount*good_price)

def main():
  is_cheap, buy_amount,good_price = buy()
  talk(is_cheap,buy_amount)
  purchase_record(is_cheap,buy_amount,good_price)

if __name__ == '__main__':
  main()

# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
