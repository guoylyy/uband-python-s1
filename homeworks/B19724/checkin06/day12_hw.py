#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY
def main():
	tup = (1,2,3,4)

	print tup
	#取值
	print tup [1]
	#切片
	print tup [0:3] #取值前开后闭 包括逗号，
	print tup [0:] #取值到最后
	print tup [:1] #最开始开始取值
	#是否存在某值
	print (1 in tup) #True
	print (5 in tup) #Fales
	#赋值
	a,b,c,d = tup
	print a,b,c,d #并列打印
	print b
	print c
	print d
	#遍历
	for item in tup:
		print item 
	print '-----'
	for index, item in enumerate(tup):
		print index
		print item
	#报错尝试
	#不支持 1）插入 2）修改 3）删除
	try:
		#tup.append(5)  #'tuple' object has no attribute 'append'
		#tup [1] = 'a' #'tuple' object does not support item assignment
		#del tup [0] #'tuple' object doesn't support item deletion
		pass
	except Exception as e:
		raise e


if __name__ == '__main__':
	main()