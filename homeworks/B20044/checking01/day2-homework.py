#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx


# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

 #01.int   
def main():
 apple_number = 5
 print '苹果有%d 个'% (apple_number)

 apple_price = 4.8
 print '苹果价格为%g 元'% (apple_price)

 pie_number = 6
 print "派有%d 个"% (pie_number)

 pie_price = 6.7
 print '派的价格为 %g 元'% (pie_price)


 #02. *  /
 apple_number = 5
 apple_price = 4.8
 apple_total_price = apple_number * apple_price

 print '苹果总价为%d元' % (apple_total_price)


 pie_number = 6
 pie_price = 6.7
 pie_total_price =pie_number * pie_price

 print '派的总价为 %0.2f元' % (pie_total_price)



 pie_number = 6
 pie_total_price =40.2
 pie_price=pie_total_price/pie_number  

 print '派的单价为 %g元' % (pie_price)

   #03. try to explain what's float
 print 'pie cost %d ' % (pie_total_price)   #整数
 print 'pie cost %g ' % (pie_total_price)   #输出小数点后宽度最小的,去除不必要的零
 print 'pie cost %0.2f ' % (pie_total_price) #保留小数点后两位


 #04. ** （幂：x的y次幂）
 number = 2**3    #表示2的3次方
 print 'number = %d' % (number) #记住，只要print里面有数字，后边一定要跟一个（）来表示什么数值。


# #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算


#一、用test的话主要是判断真假→真1假0  最后都是一个数值 因为用的是print '%d'()的格式

#()内可以直接是数值，也可以是未知数xy的计算，但是前面要先对xy赋值

 print 'test: %d' % (1 != 2) #比较是否不相等  真为1，假为0  此为真1

 print 'test: %d' % (1 >= 2)  #假

 print "test: %d "% (2==2) #比较是否相等→真

#或者是给出一个数值
# print'test: %d'% (8%5) #取模，即返回除法的余数  只是一般不这么写吧

 
 # print 'test:xxx'(1 !=2 )这种算法是错误的，因为 1必然不等于2，所以只能判断真假，不能输入数值（一开始的想法错了）
 #改：错误的原因应该是说test用来判断真假或者给出数值，用数值%d来表示。但这里没有数值。



#if(1!=2):
   #print 'test:xxx''就成立    
   #1如果1不等于2成立，
        #那么命题为真1，
        #打印test:xxx这些符号
   #2如果不成立，就不打印 

#二、if条件后的print不要求是数值。 （针对计算而言）   if条件→判断真假→print   反正满足条件就答应，可以是文字，也可以是字符。
#但如果是数值的话必定要用%d（）形式，或者直接给出数字。


#总结，只要是数值，要么就是直接的数字，要么就是%d（）形式。

#相反，有数值的话反而变成了print'%d'()的格式，就变成上面那种形式，这样的话也就不用用if了。
#这只是针对计算，有些代值的语言还是可以用print'%d'()的格式的。
#比如if is_cheap =True:
#   print "%d"%(buy_amount)
#说明也不是说print后面就不能是数值，这里只是针对计算而言

 if 1: #真→执行
    print 'goog' #

 if 0: #假→不执行
    print 'xxx'

 if(2 != 2):#是否不相等→否→所以不print
    print 'wweewe we w'

 #if (1 !=2 ):
 	#print 'test:%d' %
 	#这种算法是错误的，可能因为if后没法test出真假？
 	#不是，其实关键是print里面出现了一个数值后，后面必须有（）来给他赋值，即print 'test:%d' %（1！=2）
 	#这样的话，前面的if也就没有必要了

 #if(1!=2):
   #print 'test:xxx''就成立，因为这里print里面不需要数字，所以后面也不用有().




  #请开始你的表演

 a=2
 b=3
 print "a+b=%d"% (a+b)

 print '5-6=%d'%(5-6)

 print '2*3=%d'%(2*3)

 print '2**3=%d'%(2**3)

 print '3/2=%g'%(3/2)

 print '7//2=%d'%(7//2)#取商的整数部分→取整除

 print 'number =%d'% (7%2)#取商的余数部分→取模

#x=3,y=6跑不通，要分栏
 x=3
 y=6
 print 'test=%d'%(x<y)

 x=3
 y=6
 print 'test=%d'%(x>y)

 x=3
 y=6
 print 'test=%d'%(x<=y)

 x=3
 y=6
 print 'test=%d'%(x>=y)


 print 'test=%d'%(1==3)

 print 'test=%d'%(1!=3)

 x=True
 print 'test=%d'%(not x)


 x=True
 y=not x
 print 'test=%d'%(y)

 x=False
 y=True #可写可不写
 print'test=%d'%(x and y)

 x=True
 print'test=%d'%(x or y)





if __name__ == '__main__':
  main()
