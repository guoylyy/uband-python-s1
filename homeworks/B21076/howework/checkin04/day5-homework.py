#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Mansur

#1. list 你的理解？有什么用
#list就是C语言里的数组或链表，用来放置对象，这里的对象可以是同一类型，也可以是不同类型。用处就是用于便于管理这类对象

# 2. for 有什么用
# for是循环语句，一般用来做一些重复动作

def main():
	lst=['白菜','萝卜','西瓜','牛肉','猪肉']
	for lst_item in lst:
		print lst_item 
	print '---------'
	lst2=['白菜',14,False]
	for lst2_item in lst2:
		print lst2_item

if __name__ == '__main__':
	main()