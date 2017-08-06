#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	tup=('a','b','c','d')
	print tup[0]
	try:
		tup[1]='test'
	except Exception, e:
		print e
	print tup
	

if __name__ == '__main__':
  main()