#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author:SKY
# Day02 homework

def main():
	#01. int 
	apple_number=5
	apple_price=4.8
	pie_number=6
	pie_price=6.7

	#02. *
	# 乘运算
	# 当一个字符进行*运算时，相当于进行复制
	str='a'*4;
	apple_total_price=apple_number*apple_price
	pie_total_price=pie_number*pie_price

	#03. 以不同格式输出
	print 'str = %s ' % (str)
	# 整型输出
	print 'pie cost %d ' %(pie_total_price)
	# %g 根据数据大小自动采用%e（科学计数法） 或者 %f（浮点型）,
	# 不知怎么= =，测试并没有成功
	print 'pie cost %g ' %(pie_total_price)
	print 'pie cost %g ' %(3.99990002*4.9999)
	# 浮点数计算，可以规定保留几位小数
	print 'pie cost %0.2f ' % (pie_total_price)
	print 'pie cost %0.1f ' % (pie_total_price)

	#04. **
	#平方运算符
	number=2**3
	print 'number = %d ' %(number)
	
	#05. +/-
	#加法是两个对象相加
	print '1+2 = %d' % (1+2)
	# 如果是两个字符相加，得到相连的字符串
	print 'a + b = %s ' %('a'+'b')
	# -，减法运算符或者负数标志
	print ' 表示负数 %d ' % (-5)
	print '4 - 3 = %d ' % (4-3)

	#6. / 除法
	#整型数据获得整型结果，浮点型数据获得浮点型结果，只要除数和被除数中有一个浮点型
	print '6 / 4 = %d ' % (6/4)
	print '6 / 4 = %f ' % (6/4) # 这里将输出格式转化为浮点型，可以看到输出的是计算后得到的整型数据又转化为浮点型的
	print '6.0 / 4.0 = %d' % (6.0/4.0) #这里将输出转化为了整型，小数部分便不显示
	print '6.0 / 4.0 = %f' % (6.0/4.0)

	#7.//取整除和%取模
	#//获得商的整数部分 ， 5 获得商的余数部分
	print '9 / 4 商 %d 余数为 %d ' %(9//4,9%4)

	#8.左移<<和右移>>
	#把一个数的比特向左或者右移动一定数目
	#比如3的二进制表示为 11 ，3<<2 变为 1100--12
	#3>>1 11变为1，最右边的1，去掉
	print '3左移两位为 %d ' %(3<<2)
	print '3右移一位为 %d ' %(3>>1)

	#9.位运算 按位与&、按位或|，按位异或^、按位翻转（取反）~
	#按位与& ，5&3=1，转换为二进制进行计算，0101&0011=0001----两个1相与得1，其余得0
	print '5 & 3 = %d ' % (5&3)
	#按位或| , 5|3=7  ,--0101|0011=0111------两个0相或得0，其余得1
	print '5 | 3 = %d ' %(5|3)
	#按位异或^,5^3=6  ,--0101^0011=0110------不同得1，相同得0
	print '5 ^ 3 = %d ' %(5^3)
	#按位翻转~  ~5=6  ，`0101=1010
	print '~5 = %d ' %(~5)
	
	#10. 比较运算符
	#<,>,<=,>=,==,!=
	#返回值为bool
	print (3>5)
	print (3<6)
	print (3>=3)
	print (2<=1)
	print (1!=1)
	print (2!=1)

	#11.not ,and ,or
	#not 相当于取反，true变FALSE，FALSE变TRUE
	#and ，且，x and y ,当X为TRUE则返回Y的计算值（或者逻辑值），否则返回FALSE
	#or ,或，x or y 当X为TRUE ,返回TRUE,否则返回Y的计算值（或逻辑值）
	#在Python中TRUE默认为1，FALSE默认为0
	print (True and (1+1))
	print (True and (1>3))
	print (True+4)
	print (False or (1+1))
	print (True or (1+1))


if __name__=='__main__':
	main()