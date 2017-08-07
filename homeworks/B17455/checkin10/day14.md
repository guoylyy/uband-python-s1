#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

Day14_week2 复盘
1）整理目前学到的东西  
三个数据结构：列表、字典、元组
列表：序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字或索引，第一个索引是0，第二个索引是1，依此类推。
      序列都可以进行的操作包括索引，切片，加，乘，检查成员。
      列表的数据项不需要具有相同的类型创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。

字典：字典是另一种可变容器模型，且可存储任意类型对象。
      字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
      d = {key1 : value1, key2 : value2 }
      键必须是唯一的，但值则不必。没有索引顺序。
      print dictionary.keys() #获取key的列表
      print dictionary.values() #获取vlaues的列表
      print dictionary.has_key('good') #有
      print dictionary.clear() 

      for key in dictionary.keys():
      	print key
      	print dictionary[key]

元组：Python的元组与列表类似，不同之处在于元组的元素不能修改。
      tup = (1,2,3,4)
      for index, item in enumerate(tup):
      	print index
    元组运算符：
    # 是否存在某值
      print (1 in tup)
      ('Hi!',) * 4


异常处理： try/except 语句
捕捉异常可以使用try/except语句。 
try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。 
如果你不想在异常发生时结束你的程序，只需在try里捕获它。
    try:
    tup[0] = 'aaa'  #修改失败
     # tup.append(9) #插入失败
     # del tup[0]    #删除失败 'tuple' object doesn't support item deletion
    except Exception, e:
     print e

“Don’t repeat yourself” 原则是通过建立变量，或者，建立调用函数，代替重复的参数或者操作。
从而提高编程效率，清晰思路。


2）整理学习所犯的错误以及当时的思维过程
在day13作业中写的是老妈去商店买东西，根据商店货物有无情况输出是否买到相应货物的结果。
一开始设定了很多参数：shopping_lst，good_lst。check_lst，final_lst...
还用了两个迭代访问用来判断输出：
for index, lst_item  in enumerate(shopping_lst): 
for index, is_check in enumerate(check_lst):

最后考虑到“Don’t repeat yourself” 原则实现了代码简化：
	for index, lst_item  in enumerate(shopping_lst):

		if (lst_item in good_lst):
			check_lst[index] = True
		else:
			check_lst[index] = False

		try:
			check(check_lst,index,shopping_lst)
		except Exception,e:
			print '错误:%s：%s' % (e,shopping_lst[index])