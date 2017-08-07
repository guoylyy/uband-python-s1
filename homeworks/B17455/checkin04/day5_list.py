#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

#list数据结构 for循环语句


def main():
	good1 = '大白菜'
	good2 = '空心菜'
	good3 = '花菜'
	good4 = '生姜'
	good5 = '小龙虾'

	print '老妈看到了 %s ' % (good1)
	print '老妈看到了 %s ' % (good2)
	print '老妈看到了 %s ' % (good2)
	print '老妈看到了 %s ' % (good4)
	print '老妈看到了 %s ' % (good5)

def main2():
	goods = '大白菜，空心菜，花菜， 生姜，小龙虾'
	pass

	#print '老妈看到了 %s ' % (goods)

def main3():
	lst = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾'] #列表


	

	for lst_item in lst: #遍历
		print '老妈在菜场看到了 %s '% (lst_item)

	print '总共看到了%d样菜' % (len(lst))

	print 'These items are:', # Notice the comma at end of the line
	for item in lst:
		print item, #magical comma！！！不用换行啦哈哈！

	print '\n老妈想起来还要买大蒜呢'#上面不用换行啦下面就要加上换行的转义符号啦

	lst2 = ['dabaicai', 'kongxincai', 'huacai', 'shengjiang', 'xiaolongxia'] #列表

	lst2.append('dasuan')
	print lst2

	print '老妈买完了%s' % (lst[0])
	del lst2[0]
	print '现在剩下的菜就是', lst2

	for item in lst2:
		print item, 


def main4():


	lst2 = ['dabaicai', 'kongxincai', 'huacai', 'shengjiang', 'xiaolongxia'] #列表

	# Indexing or 'Subscription' operation
	print lst2[0]
	print lst2[-1]


	# Slicing on a list
	print '老妈看到的第1到3的菜是', lst2[0:3]
	print '老妈看到的第2到最后的菜是', lst2[2:]
	print '老妈看到的第2到最后的菜是', lst2[3:-1]
	print '老妈看到的第2到最后的菜是', lst2[:]

	# Slicing on a string
	name = 'ubandfrancie'
	print 'characters 1 to 3 is', name[1:3]
	print 'characters 2 to end is', name[2:]



if __name__ == '__main__':
#	main()
	# main2()
	main4()