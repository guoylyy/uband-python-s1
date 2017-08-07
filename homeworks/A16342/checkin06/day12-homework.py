#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

def main():
	tup = (1,2,3,4)

	#取值
	print tup[1]

	#切片
	print tup
	print tup[0:3]
	print tup[2:]

	#是否存在某值
	print (1 in tup)
	print (5 in tup)

	#赋值
	a,b,c,d = tup
	print a
	print b
	print c
	print d

	#遍历
	print '-------'

	for item in tup:
		print item

	print 'enumerate------'

	for index, item in enumerate(tup):
		print index
		print item

	print '--------'
	#报错
	try:
		#tup.append(9)   #'tuple' object has no attribute 'append'
		#del tup[0]			#'tuple' object doesn't support item deletion
		#tup[0] = 'aaaa'		#'tuple' object does not support item assignment
		pass
	except Exception,e:
		print e

if __name__ == '__main__':
	main()