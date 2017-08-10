#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
#元祖和列表的区别
#元祖是稳定的，无添加无修改无删除
def main():
	tup=(1,2,3,4)

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
	a,b,c,d=tup #a,b,c,d=1,2,3,4
	print a
	print b
	print c
	print d

	print'-------------'
	for item in tup:
		print item
	for index,intem in enumerate(tup):
		print index
		print item
	print'--------------'
	#花式报错
	#不支持 插入 修改和删除等操作
	#try:
		#tup.append(9) 跑程序失败，插入失败
		#del tup[0]  跑程序失败，删除失败
		#tup[0]='aaa'#修改失败
if __name__ == '__main__':
	main()