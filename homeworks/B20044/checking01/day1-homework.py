#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu


# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print




# 1. 对照锅蜀黍的代码自己打一遍

#总结：1.基本量
      #2.设置场景
      #3.分情况讨论:if else

def main():
#首先写入一些基本的量
 who= '锅蜀黍的老妈'
 good_price=6
 good_description ='西双版纳大白菜'

 is_cheap = False  #这里先要设置False
 reasonable_price=5
 buy_amount = 2

#给出一个场景
 print "%s上街看到了%s，卖%d元/斤" % (who,good_description,good_price) #文字%s后面也要加%

 #开始假设某种情况成立，或者不成立会出现何种结果。

 if good_price <= reasonable_price:
	print '她认为便宜'#其实这是一种原因，因为便宜，才买x斤→这就是逻辑
	is_cheap=True
	print '她买了%d斤' % (buy_amount)

 else:
	print "她认为贵了"
	is_cheap=False
	print "她并没有买，扬长而去"


# run function
if __name__ == '__main__':
  main()

# 2. 把锅蜀黍的老妈改成你老妈，跑通

def main():
 who= '奇葩姐的老妈'
 good_price=6
 good_description ='西双版纳大白菜'

 is_cheap = False
 reasonable_price=5
 buy_amount = 2


 print "%s上街看到了%s，卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
	print '她认为便宜'
	is_cheap=True
	print '她买了%d斤' % (buy_amount)

 else:
	print "她认为贵了"
	is_cheap=False
	print "她并没有买，扬长而去"


# run function
if __name__ == '__main__':
  main()





# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）

#good_price=5比修改resonable_price好，因为前者是外部；后者是内部的，难改。

def main():
 who= '奇葩姐的老妈'
 good_price=5
 good_description ='西双版纳大白菜'

 is_cheap = False 
 reasonable_price=5 
 buy_amount = 2


 print "%s上街看到了%s，卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
	print '她认为便宜'
	is_cheap=True
	print '她买了%d斤' % (buy_amount)



 else:
	print "她认为贵了"
	is_cheap=False
	print "她并没有买，扬长而去"

# run function
if __name__ == '__main__':
  main()
#不一定每一个都要def,if，可以组成def main,main2, 最后再用一个if 


# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
#what's the meaning of 'number', 'string', 'boolean' in python?
#number是数字，string是字符串，比如中英文那些描述。boolean是布尔逻辑中的“真”和“假”，指true和false，是一种判断条件。

#try to describe the meaning of 'if' statement in your mind?
#if是一种判断条件，表示满足某种条件就会出现怎样的结果。

#Why we need > < == >= <= ...etc...?
#因为条件不一定全都是符合某个具体数字，也可能是一个特定的区间。为了表示数字的范围，作为if后面的条件。如果满足这个区间，就会出现什么结果。

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来

def main():
 who= '奇葩姐的老妈'
 good_price=2
 good_description ='西双版纳大白菜'

 is_cheap = False
 reasonable_price=5
 buy_amount = 2


 print "%s上街看到了%s，卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price: #reasonable总是忘了a字母
    print '她认为便宜'#不能和If对齐，因为是if内的一部分
    is_cheap=True   
    #5-2 4-3 3-4   /2-4  1-4
    #每低1元，多买1斤
    #多买了几斤=减价了多少钱
    #现在买的总斤数-最基础的斤数2斤=原价5元-现在便宜后的价格
    #buy_amount-2=5-good_price
    buy_amount=7-good_price

    if buy_amount>4:
	     buy_amount=4 

    print '她买了%d斤. ' % (buy_amount)#如果不对齐也出错   ？
    #初步设想，上面的If是和else对齐的，所以到print的时候要缩进，是if内的小部分
    #下面这里的if和print是平行部分？？？
	
    #求解答
    #原因是print的这句话其实是不归这里的小if管的。如果和buy_amount缩进相同，则归if buy_amount>4管。
    #但事实上，即使buy_amount<=4,我们也仍然要写她买了多少斤
    #它是属于if good_price<=reasonable_price管的


#【回答奇葩姐】 如果你放到if里面，就是只有 满足if条件的时候才能print
#if 管理了if后面缩进的后面的代码块，如果你没有放在if后面的一个缩进里，if就管不了她
#管不了他，他就print了哦
#还有空行是无所谓的，空 100 行，实际python跑的时候会忽略空行
#因为我之前把print的这句话看成了if buy_amount>4的一部分，但其实它不是这里面的。

 else:
    print "她认为贵了"
    is_cheap=False
    print "她并没有买，扬长而去"


# run function
if __name__ == '__main__':
 main()

