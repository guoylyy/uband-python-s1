#!/usr/bin/python
#-*-coding:utf-8-*-
#@author:suancaiyu

#学习内容：
#1，元祖 tuple  定义，作为python 数据结构之一的元祖有哪些方法？支持像列表和字典一样的方法操作吗？
#try:			except :

def main():
#定义
	tup=(1,2,3,4,5)
#取值
	print tup[3]
	print tup[0:3]
	print tup[2:]
#判断值是否存在 	
	print  (1 in tup) # 返回的值为bool类型
	print	(5 in tup)
#赋值
	a,b,c,d,helo=(1,2,3,4,5)
	print a
	print b
	print c
	print d
	print helo

	print '-------'

	for item in tup:
		print item

	print 'enumerate---'

	for index,item in enumerate(tup):
		print index

	print '-------'
#try
#	try:
#		tup.append(9)
#		del tup[0]
#		tup[0]='aaa'
#	except Exception,e:
#		print e


if __name__=='__main__':
	main()
