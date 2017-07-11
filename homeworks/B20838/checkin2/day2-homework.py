#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO

def main():
    #01.int	
	pie_number = 6
	pie_price = 6.8
 
	#02.*乘
	pie_total_price = pie_number * pie_price

	#03.1整数的输出
	print 'pie cost %d' % (pie_total_price) #十进制
	print 'pie cost %x' % (pie_total_price) #十六进制
	print 'pie cost %o' % (pie_total_price) #八进制

	#3.2浮点数的输出
	print 'pie cost %f' % (pie_total_price) #默认情况下最多保留6位有效数字
	print 'pie cost %0.2f' % (pie_total_price)
	print 'pie cost %g' % (pie_total_price)
	print 'pie cost %e' % (pie_total_price)

	#04.**幂（返回X的Y次幂）
	number = 3.1 ** 4
	print 'number = %g' %(number)

	#05./除（X除以Y）
	number = 10.5 / 5
	print 'number = %g' %(number)

	#06.//取整除（返回商的整数部分）
	number = 13 // 3
	print 'number = %d' %(number)

	#07.%取模（返回除法的语数）
	number = 13 % 3
	print 'number = %d' %(number)

	#08.左移<<（把一个数的比特向左移一定数目）
	number = 2 << 2
	print 'number = %d' %(number)
	number = 2 << 3
	print 'number = %d' %(number )

	#09.右移>>
	number = 11 >> 1
	print 'number = %d' %(number)
	number = 12 >> 1
	print 'number = %d' %(number)

	#10.按位与&
	number = 5 & 3
	print 'numebr = %d' %(number)
	numebr = 5 & 8
	print 'numebr = %d' %(number)
	number = 5 & 6
	print 'numebr = %d' %(number)

	#11.按位或| 
	number = 5 | 3
	print 'numebr = %d' %(number)

	#12.按位异或^
	number = 5 ^ 3
	print 'numebr = %d' %(number)
	print 'test %d' % (5^3)

	#13.按位翻转~(X的按位翻转是-（X+1）)
	number = ~ 5 
	print 'numebr = %d' %(number)
	print 'test %d' % (~6)
	#14.
	print 'test: %d' % (1 > 2 )
	print 'test: %d' % (1 < 2)
	print 'test: %d' % (1 != 2)
	if 1:
		print '对啦'
	else:
		print '错啦'

	print 'test: %d' % (1 == 2)


if __name__ == '__main__':
	main()
