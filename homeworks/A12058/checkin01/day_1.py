# -*-coding: utf-8 -*-
# @author: Shuan




# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
def main():
 who = '栓妈妈'
 good_price = 6
 good_description = '西双版纳大白菜'
 is_cheap = False
 reasonable_price = 5
 buy_amount = 2

 print"%s上街看到了%s卖%d元/斤"% (who, good_description, good_price)
 if good_price <= reasonable_price:
  print' 她认为便宜 '
  is_cheap= True
  print'她买了%d斤 '(buy_amount)
 else :
  print'她认为贵了 '
  is_cheap= False
  print'她并没有买，扬长而去 '
 
if __name__ == '__main__':
 main()


# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 方案一
def main():
 who = '栓妈妈'
 good_price = 6
 good_description = '西双版纳大白菜'
 is_cheap = False
 reasonable_price = 5
 buy_amount = 2

 print"%s上街看到了%s卖%d元/斤"% (who, good_description, good_price)
 if good_price >= reasonable_price:                                          #<=改成>=
  print'她认为便宜 '
  is_cheap= True
  print'她买了%d斤 '%(buy_amount)
 else :
  print'她认为贵了 '
  is_cheap= False
  print'她并没有买，扬长而去 '
 
if __name__ == '__main__':
 main()

 # 方案二
 # -*-coding: utf-8 -*-
# @author: Shuan

def main():
 who = '栓妈妈'
 good_price = 6
 good_description = '西双版纳大白菜'
 is_cheap = False
 reasonable_price = 8                                    #提高reasonable price价格，使之大于6
 buy_amount = 2

 print"%s上街看到了%s卖%d元/斤"% (who, good_description, good_price)
 if good_price <= reasonable_price:                                        
  print'她认为便宜 '
  is_cheap= True
  print'她买了%d斤 '%(buy_amount)
 else :
  print'她认为贵了 '
  is_cheap= False
  print'她并没有买，扬长而去 '
 
if __name__ == '__main__':
 main()

#4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# what's the meaning of 'number', 'string', 'boolean' in python?
#number是指数字变量，string是字符变量，boolean是是用来返回真假的

#try to describe the meaning of 'if' statement in your mind?
#if可以表示一种条件筛选，用一定的条件来对应两种或多种不同的结果

#Why we need > < == >= <= ...etc...?
#用来比较数值的大小，或者字符串是否相同，还可以比较字符串长度

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来

def main():
 who = '栓妈妈'
 good_price = 2
 good_description = '西双版纳大白菜'                       
 reasonable_price = 5

 mom_price=good_price
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

if __name__ == '__main__':
 main()