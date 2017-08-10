#!/usr/bin/python
# -*- coding: utf-8 -*-


def main1():
	good1='cabbage'
	good2='spinach'
	good3='cauliflower'
	good4='ginger'
	good5='lobster'

	print 'mom see %s'%(good1)
	print 'mom see %s'%(good2)


def main2():
	goods='cabbage,spinach,cauliflower,ginger,lobster'
	print 'mom see %s'%(goods)

def main3():
	lst=['cabbage','spinach','cauliflower','ginger','lobster']
	for lst_item in lst:
		print 'mom see %s'%(lst_item)
		

if __name__ == '__main__':
	main1()
	main2()
	main3()





