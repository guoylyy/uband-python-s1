#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:闪电

def main():
	tup = (1,2,3,4)
	#取值
	print tup[3]
	print tup	
	print tup[0:3]
	print tup[0:4]
	print tup[0:]
	#切片
	print tup[2:4]
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
	print '--------'
	for item in tup:
		print item
	print '--------'
	for index,item in enumerate(tup):
		print index
		print item
	print '--------'
	#不支持 插入 修改 删除
	try:
		#tup.append(8)
		#del tup[0]
		tup[0] = 'aaa'
	except Exception,e:
		print e




if __name__ == '__main__':
	main()