#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

# homework 1
def shopping():
	print 'Mom went to the market.'
	lst = ['Chinese cabbage', 'turnips', 'tomatoes', 'fish', 'lobsters', \
	 'ginger', 'sweet potatoes', 'grapefruit', 'beef', 'jiaozi' ]
	for index, lst_item in enumerate(lst):
		if index%2 == 0:
			print 'She saw some %s and bought %d jin.' % (lst_item, index+1)
		else:
			print 'She saw some %s and did not buy any.' %(lst_item)
		print 'She went on shopping.'

# homework 2
	lst.append('carrot' )
	lst.append('baozi')
	lst.append('broccoli')
	print len(lst)

	return lst
	
# homework 3
def shopping_1(lst):
	print "------"
	lst_1 = lst[5:10]
	print 'Mom went to the market.'
	for index, lst_item in enumerate(lst_1):
		if index%2 == 1:
			print 'She saw some %s and bought %d jin.' % (lst_item, index+6)
		else:
			print 'She saw some %s and didnot buy any.' %(lst_item)
		print 'She went on shopping.'

def main():
	lst = shopping()
	shopping_1(lst)

if __name__ == '__main__':
	main()