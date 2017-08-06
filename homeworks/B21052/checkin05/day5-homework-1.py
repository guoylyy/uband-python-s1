#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def main():
	good_1 = 'cabbage'
	good_2 = 'tomato'
	good_3 = 'cucumber'
	good_4 = 'bean'
	good_5 = 'carrot'

	#------One hundred items are omitted.
	good_100 = 'potato'

	print 'My mum saw %s in the vegetable market.' % (good_1)
	print 'My mum saw %s in the vegetable market.' % (good_2)
	print 'My mum saw %s in the vegetable market.' % (good_3)
	print 'My mum saw %s in the vegetable market.' % (good_4)
	print 'My mum saw %s in the vegetable market.' % (good_5)

def main2():
	goods = 'cabbage, tomato, cucumber, bean, potato'
	print 'My mum saw %s in the vegetable market.' % (goods)
 
def main3():
	print '-----------------------------------------'
	lst = ['cabbage', 'tomato', 'cucumber', 'bean', 'potato']  
	for lst_item in lst:
		print 'My mum saw  %s in the vegetabel markrt.' % (lst_item)

if __name__ == '__main__':
  main()
  main2()
  main3()