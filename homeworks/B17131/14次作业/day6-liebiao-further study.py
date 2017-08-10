#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt
#列表深入学习
#list: 排排坐，吃果果
#for: 像银行柜员一样1号，2号，3号，4号，5号。。。
def print_list(lst):
	for lst_item in lst: #遍历
		print '老妈看到了%s'%(lst_item)

def main():
	#      0        1        2      3      4
	lst = ['大白菜','空心菜','花菜','生姜','小龙虾'] #列表
	#循环访问
	for lst_item in lst: #遍历
		#print '老妈看到了%s' % (lst_item)
		pass

	#记录下标（相当于给每个物品标上号一样，比如说大白菜就是“第0个”。。。以此类推）
	index = 0
	for lst_item in lst: #遍历
		#print '当老妈看到了%s' %(lst_item)
		#print '当前第%d个' %(index)
		index = index + 1

	#迭代访问(比记录下标更加简便，却能达到相同的效果) 
	#enumerate就是内置函数，就是既能返回第一个lst里的值，又能返回第二个index里的值。而如果只有第二个for的话，它只能返回lst.
	for index, lst_item in enumerate(lst):
		#print '当老妈看到了%s' %(lst_item)
		#print '当前第%d个' %(index)
		pass

	#取值
	#print lst[0] #0-大白菜
	#print lst[1] #1-空心菜

	#长度(表明列表里面有几个元素)
	print len(lst) #比如说这里跑通以后会出来数字5，因为有5个元素

	#加(想在列表里加上某个元素的话，比如这里就是就是加上了白芍)
	lst.append('白芍')
	print_list(lst)

	#删除(删除列表里某个元素)
	#del lst[0] #在这里就是去掉大白菜
	print '----'
	#print_list(lst)

	#切片
	lst2 = lst[0:3] #取0，1，2 冒号左边那个元素是包括的，直到冒号右边那个前面一个元素为止。比如[2:5]的意思就是2，3，4
	print_list(lst2)


if __name__ == '__main__':
		main()	
