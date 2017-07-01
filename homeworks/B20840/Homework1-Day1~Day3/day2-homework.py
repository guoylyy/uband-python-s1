#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author: B20840

#Day2 - 为了大家能够做好这一次的第一个作业
#		继续深化变量的练习
#
#homework2

def main():
	#01.int
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	#02. */
	apple_total_price = apple_number*apple_price
	pie_total_price = pie_number* pie_price

	#03.try to explain what's float
	print 'pie cost %d' %(pie_total_price)
	print 'pie cost %g' %(pie_total_price)
	print 'pie cost %0.2f' %(pie_total_price)

	#04.**
	number = 2**3
	print 'numer = %d' %(number)

	#05. what else?
	#	在Python简明教程中找到第34页，然后搞懂所有的符号
	#	每个符号在限免测试一下 除了<< >> ^ ~几个不用理解，之后会讲
	#	不用理解优先级，只用记住一句话：括号里面的最先计算
	print 'test: %d' %(1!=2)
	print 'test: %d' %(1>=2)
	if 1:
		print 'goog'
	if 0:
		print 'xxx'

	if (2!=2):
		print 'wweewe we w'
	#请开始你的表演

	print 'result of plus: %d' %(9+16)
	print 'result of minus: %d' %(9-100)
	print 'result of multiplication %d' %(4*6)
	print 'result of multiplication: %s' %('python '*2)
	print 'result of cloth: %d' %(2**7)
	print 'result of division: %d' %(4/6)
	print 'result of division: %d' %(49/6)
	print 'result of division: %f' %(50.00/7.00)
	print 'result of division: %d' %(4/6)
	print 'result of division: %d' %(168/6)
	print 'result of test: %f' %(-25.5%2.25)
	print 'result of binary test: %d' %(2<<7)
	print 'result of binary test: %d' %(11>>1)
	print 'result of binary test: %d' %(192&225)
	print 'result of binary test: %d' %(192|255)
	print 'result of binary test: %d' %(5^3)
	print 'result of binary test: %d' %(~6)
	print 'test: %d' %(5<3<9)
	print 'test: %d' %(5>3)
	print 'test result is: %d' %(3<=6)
	print 'test result is: %d' %(4>=3)
	print 'test result is: %d' %(2==2)
	print 'test result is: %d' %('kilo'=='kilo')
	print 'test result is: %d' %(3!=3)
	print 'test result is: %d' %(not True)
	print 'test result is: %d' %(True and True)
	print 'test result is: %d' %(True or False)









if __name__=='__main__':
	main()









