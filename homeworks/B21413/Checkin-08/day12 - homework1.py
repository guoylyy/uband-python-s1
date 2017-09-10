#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 190

def main():
	tup = (1,2,3,4)

	print '______'

	print tup[3] #根据index取值

	print tup
	print tup[0:2] #取值
	print tup[3:]

	print (2 in tup) #元组内是否存在某值的判断
	print (9 in tup)

	e,f,g,h = (1,2,3,4) #给元组赋值
	print e
	print f
	print g
	print h

	print '______'

	for item in tup: #遍历的尝试，在元组内是ok的
		print item

	for index,item in enumerate(tup): #类似列表，同时下标的enumerate命令也是可行
		print index

	print '______'

	#那什么不可行呢？
	# 不支持 1）插入 2）修改 3）删除
	try:
		#tup.append(6), 出错了
 		#del tup[2] 又报错
 		#tup[2] = 'you' 再次跪了
 		pass
	except Exception,e:
		print e


if __name__ == '__main__':
  main()