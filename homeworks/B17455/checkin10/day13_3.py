#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455
def print_list(lst):
	for lst_item in lst:
		print lst_item,

def buy():
	who = 'MOM'
	shopping_lst = ['watermelon', 'tomato', 'icecream', 'meat','salt']
	good_lst = ['watermelon', 'tomato', 'meat','salt']
	num = len(shopping_lst)
	check_lst = [None]*num

	print '今天%s打算去买的东西有：' % (who)
	print_list(shopping_lst)
	print '\n商店里货不全，所以'
	
	for index, lst_item  in enumerate(shopping_lst):

		if (lst_item in good_lst):
			check_lst[index] = True
		else:
			check_lst[index] = False

		try:
			check(check_lst,index,shopping_lst)
		except Exception,e:
			print '错误:%s：%s' % (e,shopping_lst[index])

def check(check_lst,index,shopping_lst):
  if check_lst[index]:
  	 print '买到了%s' %(shopping_lst[index])
  else:
  	raise Exception('商店没货没买到的是')  #强行中断程序的语法'

if __name__ == '__main__':
	buy()