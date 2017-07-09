#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下

def  talk_with_daddy (is_cheap3,buy_amount3):    #切记（）里要写return里需要的量，但也不是全写，看板块里需要什么。

 if is_cheap3:       #if后面切记加冒号，少了个3上下不一致的话又会出错，意思是说要和def（）里面的值符号相同
  print "老妈回到家里,跟老爸说:'今天去买菜,价格不贵,买了%d斤.'"% (buy_amount3)
 else:
  print"老妈回到家里，跟老爸说:'今天去买菜,菜好贵额,没买.'"

def record_account (is_cheap,buy_amount,good_price): #冒号容易漏  is_cheap容易漏，忘了还有这个量   从要print的内容入手，找需要的变量

  if is_cheap:#容易忘写is_cheap
  	print "老妈在小本子记了买了%d斤白菜,每斤%d元,花销%d 元" % (buy_amount,good_price,buy_amount*good_price) #我的改法是在buybuybuy里不出现总价，直到这里才开始算


def buybuybuy():

#第一大板块
 good_price=4#每降低1元，多买1斤
 reasonable_price=5#不变
 buy_amount = 2#每降低1元，多买1斤   这里可以先随便赋值，在后面的if里再运算公式就可以了。  #其实这里设置成1也无所谓，只要后面覆盖掉数值即可

  #错误解释（后来被推翻）why?
  #假设6元不买的话，如果不加上这句话就会出错
  #因为假设不买的话，else里面只有一个is_cheap,加上这里有的buy_amount就没了，
  #但是return的时候又还有return一个buy_total_price，这时候就没有了这个值。

 who= '奇葩姐的老妈'
 good_description ='西双版纳大白菜'


 is_cheap = False

 print "%s上街看到了%s，卖%d元/斤" % (who,good_description,good_price)



#第二大板块
 if good_price <= reasonable_price:
	print '她认为便宜'
	is_cheap=True
	#5元-2斤(题干说的) 4-3 3-4 2-4 1-4 
	buy_amount=2 + (reasonable_price-good_price)  #在2斤上增加   合理价格=5 在5的基础上减价
	#每减1元，多买1斤
	#买了多少斤=基础2斤+ 多买了多少斤=基础2斤+减了多少块钱=基础2斤+(原价5-现在便宜后的价钱)
    
    #被推翻  因为数值不对应  why?
	#一开始认为buy_total_price = buy_amount *good_price  写在开头或是在这里算都可以。
	#但实际上当卖6元要离开的时候，执行的只有is_cheap, 
	#然后接着进行的是return，这时就出现问题了，
	#return一定要is_cheap,buy_amount,buy_total_price  3个量
	#is_cheap else 里面有了，buy_amount开头有了，
	#但是buy_total_price，如果写在这里则只是if里面的一部分，这时候就没有了这个值。
	#所以buy_total_amount应该写在开头

	#解决方法是在print的后面再开始计算total_price
    
    #里面>4的进一步讨论，大框内的小框。
	if buy_amount>4:
	   buy_amount=4#if只管这句话

	    #写4或者buy_amount都可以，但是如果删去就不能运行
	print '她买了%d 斤.'% (buy_amount) #要和if对齐
	#原因是它不是if里面的一部分，就算买的数量<4,也要写买了几斤。

	#方法2：直接在这里算钱，但是就没有专门一个def record_amount.
	   
  #不要两个分开，写在一起


 #第三大板块
 else:
	print "她认为贵了"  #对其if的部分，因为平行
	is_cheap=False
	print "她并没有买，扬长而去"

#第四大板块

 return is_cheap,buy_amount,good_price #3个量都要一起写啊，容易漏
# run function

def main():   #用一个main来把上面3个def包括在一起。最后运算直接算main就可以了。
#其实大体的结构就是3个（）：buybuybuy(),talk_with_daddy()和record_account（）
#然后再加上buybuybuy赋值=，
#下面2个代值的过程。下面2部分其实是可谓是平行的。

#买买买
 is_cheap2,buy_amount2,good_price=buybuybuy() 
 
 #说说说
 talk_with_daddy(is_cheap2,buy_amount2)	#上下一定要相同啊，而且不要漏
 #记记记

 record_account(is_cheap2,buy_amount2,good_price)#上下一定要相同啊，如果改成了is_cheap,就又不行了，一定要和上面第一行的值相同。
 #保证一个块里面的数字相同。 不同块可以有不同。3行的数字要相同，也可以都不写。

 #上面def的顺序并不重要，真正的顺序体现在main里面的排序。

if __name__ == '__main__':  
 main ()   #最后运算直接算main就可以了。


#这里本来也可以前面def buybuy, talk,record，最后再在if里b,t,r,
#但是因为还涉及到赋值的问题，所以新建一个def main包括起来，最后是if main


#学到的东西

#(1)函数 function(code block)就是代码块
#one file→multiple function
#可以在一个文件里定义多个函数（代码块）

#(2)return (pass variable)
#把代码块里的变量传递回来→在逻辑里进行判断

#(3)return multiple variables 
#return 多个值



# 2. 解释一遍自己眼中的单一职责原则是什么？

#一个代码块职责是单一的，它只做一件事情。
#去买菜就是买买买，谈话就是谈谈谈。
#用职责去组织逻辑→编程核心的过程



# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 可以在里面计算，也可以返回来




# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
