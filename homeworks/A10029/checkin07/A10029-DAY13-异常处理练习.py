#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

def main():
	tup=(1,2,3,4,5)
	
	try:
		text(tup)#没有try语句直接运行text会在text报错，然后结束运行
	except Exception,e:#处理text异常
		print '元祖不允许添加 '	

	print tup	#处理了text代码的错误，所以这里可以继续运行


def text(tup1):
	tup1.append(6)#发生错误，元组不支持添加
	print tup1[1]#上面发生错误，这里就不运行了

if __name__=='__main__':
	main()
