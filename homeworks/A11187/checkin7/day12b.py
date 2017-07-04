#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui

def main():
	tup = (3,5,7,9)
	print tup[1]

	print tup
	print tup[0:3]
	print tup[2:]


	print '.....'
	try:
		del tup[0]
		tup [0] = 'aaa'
	except Exception, e:
		print e

if __name__ == '__main__':
	main()
