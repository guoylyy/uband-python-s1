#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

def main():
	tup=(1,2,3,4)
	print tup[1]# 取值
	print tup[1:3]# 切片

	print (1 in tup) 
	print (8 in tup)#是否存在某值

	a,b,c,d=tup
	print a, b, c, d# 赋值
	print tup
	print "-------"

	for index,item in enumerate(tup):
		print item, index
	# 遍历


	# 花式报错
	# 不支持1）插入 2）修改 3）删除
	try:
		# tup.append(1)
		# del tup(1)
		tup[3]1=5
		pass
	except Exception,e:
		print e

if __name__ == '__main__':
	main()