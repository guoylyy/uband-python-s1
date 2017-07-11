#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: erhua

def main():
	good1 = 'cabbriage'
	good2 = 'carrot'

	print 'mom saw %s '% (good1)
	print 'mom saw %s '% (good2)

def main2():
	print '------'
	lst = ['cabbriage', 'carrot', 'lobster']
	for lst_item in lst:
		print 'mom saw %s '% (lst_item)

if __name__ == '__main__':
  main()
  main2()