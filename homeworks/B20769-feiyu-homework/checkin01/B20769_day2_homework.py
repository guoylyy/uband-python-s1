#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu

def main():
	#1 + - * ** / // %
	a = 8
	b = 3
	print 'a+b=%d ;a-b=%d ;a*b=%d ;a/b=%.3e ;a**b=%d ;a//b=%d ' % (a+b , a-b , a*b , 8.0/3.0 , a**b , a//b)
	# 错误：a%b 无法正常运算
	#2 << >> & | ^ ~
	print 'a<<1=%d ;a>>1=%d ;a&b=%d ;a|b=%d ;a^b=%d ;~a=%d' % (a<<1 , a>>1 , a&b , a|b , a^b , ~a)
	#3 < >  == != <= >=
	print 'a<b=%d ;a>b=%d ;a==b=%d ;a!=b=%d ;a<=b=%d ;a>=b=%d' % (a<b , a>b , a==b , a!=b , a<=b , a>=b)
	#4 not and or
	c = 2
	d = 0
	print 'not c=%d ;not d=%d ;c and d=%d ;c or d=%d' % (not c , not d , c and d , c or d)
 
if __name__ == '__main__':
	main()
