#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

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
	a,b,c,d = (1,2,3,4)
	print a
	print b
	print c
	print d

	#遍历
	print '==========='

	for tup_item in tup:
		print tup_item

	print 'enumerate ======='
	for index,tup_item in enumerate(tup):
		print index
		print tup_item

	print 'try everything'
	# 花式报错
	# 不支持 1）插入 2）删除 3）修改


	# tup.append(9)    1）插入失败
	# del tup[1]       2）删除失败
	# tup[0] = 'aaa'   3) 修改失败

if __name__ == '__main__':
	main()