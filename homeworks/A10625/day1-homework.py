#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():	  
#2.
	print "#第2题"
	who = "鸭嘴兽的麻麻"
	good_price = 6 
	

	good_descrpetion = "西双版纳大白菜"

	

	is_cheap = False
	resonable_price = 5 
	buy_amount = 2
	#print who
	#print good_descrpetion
	#print resonable_price 
	#print buy_amount
	print "%s上街看到了%s，卖%s元一斤" % (who, good_descrpetion, good_price)
	if good_price <= resonable_price:
		print "她买了%d斤"% (buy_amount)
		is_cheap = True
	else:
		print "她觉得贵了"
		is_cheap = False
		print "她并没有买，扬长而去"

###########################################################################
	print"###########################################"
	print "#第3题方法（1）可以在good_price = 6的情况下修改为6以及6以上"
#3（1）

	who = "鸭嘴兽的麻麻"
	good_price = 6 
	

	good_descrpetion = "西双版纳大白菜"

	

	is_cheap = False
	resonable_price = 6#改为6
	buy_amount = 2
	#print who
	#print good_descrpetion
	#print resonable_price 
	#print buy_amount
	print "%s上街看到了%s，卖%s元一斤" % (who, good_descrpetion, good_price)
	if good_price <= resonable_price:
		print "她买了%d斤"% (buy_amount)
		is_cheap = True
	else:
		print "她觉得贵了"
		is_cheap = False
		print "她并没有买，扬长而去"
		#######################################
	print "#第3题方法（2）只是改变good_price 到5 或者5以下"
	who = "鸭嘴兽的麻麻"
	good_price = 5 #改为5
	

	good_descrpetion = "西双版纳大白菜"

	

	is_cheap = False
	resonable_price = 6
	buy_amount = 2
	#print who
	#print good_descrpetion
	#print resonable_price 
	#print buy_amount
	print "%s上街看到了%s，卖%s元一斤" % (who, good_descrpetion, good_price)
	if good_price <= resonable_price:
		print "她买了%d斤"% (buy_amount)
		is_cheap = True
	else:
		print "她觉得贵了"
		is_cheap = False
		print "她并没有买，扬长而去"
#############################################################
	print"###########################################"
	print"（3）价格都不修改的情况下，改变符号从小于等于到>=， 老妈就是任性，便宜没好货"
	print "#第3题方法（3）只是改变good_price 到5 或者5以下"
	who = "鸭嘴兽的麻麻"
	good_price = 6
	

	good_descrpetion = "西双版纳大白菜"

	

	is_cheap = False
	resonable_price = 5
	buy_amount = 2
	#print who
	#print good_descrpetion
	#print resonable_price 
	#print buy_amount
	print "%s上街看到了%s，卖%s元一斤" % (who, good_descrpetion, good_price)
	if good_price >= resonable_price:
		print "她买了%d斤"% (buy_amount)
		is_cheap = True
		print "便宜没好货，好货不便宜"
	else:
		print "她觉得便宜了"
		is_cheap = False
		print "她并没有买，扬长而去"
################################################################################
	print"###########################################"
	print"Question #4 见注释内容"

#string& number 
#string 就是字符串（和没说一样），对于计算机来说，应该就是文本之类的东西，貌似对于人类来说意义要比对于计算机来讲意义大很多，字符串虽然可以相加，但是不是数字意义上的相加，不具有计算的属性。 
#例如print"2"+"2" 和 #print 2+2，前者的2 就是字符串，后者的2就是数字（number）. 字符串经常出现在引号中，而数字不需要引号，并且能够进行数学意义上的运算。 比如上面的例子中，第一个是字符串的拼接，
#第二个是数字的运算。分别输入22 和4. 数字还要不同和类型可以实现不同的功能。

#Boolean 中文叫布尔型，只有两个值，是个非黑即白的死脑筋。 只有true 或者false。 一般来说，几乎一切数字类型的0，其他类型的空，都会返回false。 除了0和空和编程者特别设定为false的
#（几乎）全部会返回true

#if
#if 是一个筛子，通过条件的限制，区分不同类型，然后可以用不同的方式对不同情况。因材施教。 方便处理比较复杂的情况。 也可以利用if来开始或者结束一段程序，也可以把它当做一个开关来看。

#<>= 就是上面提到的条件，是划分的标准，是衡量的标尺。<>=是比较符。。可以通过变量的比较，是划分的具体手段。

######################################################################333

	print"###########################################"
	print"Question 5"
	who = "鸭嘴兽的麻麻"
	good_price = 6##这个变量这里可以修改
	

	good_descrpetion = "西双版纳大白菜"

	

	is_cheap = False
	resonable_price = 5 
	buy_amount = 2
	#print who
	#print good_descrpetion
	#print resonable_price 
	#print buy_amount
	print "%s上街看到了%s，卖%s元一斤" % (who, good_descrpetion, good_price)
	if good_price <= resonable_price:
		if good_price == resonable_price:

			print "她买了%d斤"% (buy_amount)
			is_cheap = True
		else:

			if good_price < resonable_price:
				if good_price > 2:#这里是解决方法一（解决办法二， 删掉这里） 

					buy_amount2 = buy_amount + resonable_price - good_price
					#if buy_amount2 <= 4（解决办法2 加上这里）
					print "她买了%d斤"% (buy_amount2)
				else:
					print "她买了4斤"
	else:
		print "她觉得贵了"
		is_cheap = False
		print "她并没有买，扬长而去"
		


########################################################################

 
if __name__ == '__main__':
  main()
