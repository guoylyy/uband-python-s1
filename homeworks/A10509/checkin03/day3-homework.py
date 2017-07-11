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

#def talk(is_cheap3,buy_amount3):
 #  if is_cheap3 = True:
  # 	   print "我今儿买了%d斤胡萝卜" %(buy_amount3)
   #else:
#   print "哼今天太贵了啥都没买吃土吧"
#这一段明明都是英文符号却怎么也不行 难过哭


def talk(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buy():
  who = "卤蛋mum"
  good_price = 4
  reasonable_price = 5
  buy_amount = 2
  food = "胡萝卜"
  is_cheap = False
  price = good_price * buy_amount
  
  print "%s上街看到%s %d一斤" %(who, food, good_price)

  if good_price <= reasonable_price:
     print "表示来%d斤" %(buy_amount)
     is_cheap = True 
  else:
     print "她觉得贵，扬长而去" 

  return is_cheap, buy_amount, price

def record(price3, is_cheap3):
	if is_cheap3:
		print "麻麻写下 胡萝卜共%d人民币" %(price3)
   	# 添了个if就是跑不通了……

def main():
	 is_cheap2, buy_amount2, price2 = buy()
	 talk(is_cheap2, buy_amount2) 
	 record(price2, is_cheap2)


if __name__ == '__main__':
  main()