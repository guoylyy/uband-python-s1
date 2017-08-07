#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

def main():
	tup = (1,2,3,4)
	print tup[1]
	print tup
	print tup[0:3]
	print tup[2:]

	print (1 in tup)
	print (0 in tup)

	a,b,b,d = tup
	print a
	print '***********'
	for item in tup:
		print item,
	print '\n************'
	for index , item in enumerate(tup):
		print index,
	print '\n************'

if __name__ == '__main__':
	main()
