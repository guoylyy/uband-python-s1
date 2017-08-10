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
	#check_lst = [True]*num
	check_lst = [None]*num
	final_lst = [None]*num

	print '今天%s打算去买的东西有：' % (who)
	print_list(shopping_lst)
	print '\n商店里货不全，所以'
	
	for index, lst_item  in enumerate(shopping_lst):

		if (lst_item in good_lst):
			check_lst[index] = True
			final_lst[index] = lst_item
		else:
			check_lst[index] = False
		
	#print check_lst
	#print final_lst

	index = 0
	for index, is_check in enumerate(check_lst):
		#check(is_check,index,final_lst)
		try:
			check(is_check,index,final_lst,shopping_lst)
		except Exception,e:
			print '错误:%s的是：%s' % (e,shopping_lst[index])

def check(is_check,index,final_lst,shopping_lst):
  if is_check:
  	 print '买到了%s' %(final_lst[index])
  else:
  	raise Exception('没买到')  #强行中断程序的语法'

if __name__ == '__main__':
	buy()