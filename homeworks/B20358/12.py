#/usr/bin/python 
# -*- coding: utf-8 -*-
# author: Anna


def main():
	tup = (1,2,3,4)

	#取值
	print tup[0]
	print tup
	#切片
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

	print '-------'

	#遍历
	for item in tup:
		print item 

	print 'e------'

	for index, item in enumerate(tup):
		print index

	print '-----'

	#花式报错
	try:
		#tup.append(9)
		#del tup[3]
		#tup[0] = 'aaa'
	except Exception, e:
		print e
		pass
	









if __name__ == '__main__':
	main()