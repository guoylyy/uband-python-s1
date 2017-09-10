# -*- coding: utf-8 -*-
# @author: 190

def main():
	print '-------'
	lst = ['dabaicai', 'kongxincai', 'huacai', 'shengjiang', 'xiaolongxia']
	for lst_item in lst:
		print 'my mom saw %s' % (lst_item)

if __name__ == '__main__':
	main()

#list 理解 = 里面的对象/数据都是独立分开的，但是却仍然可以用一个变量来表示的结构系统
#for  in 理解 = 以不断循环地访问（遍历）一个列表（变量）中各个项目，然后以逐一输出