# -*- coding: UTF-8 -*-

def print_list(lst):
	for lst_item in lst:
		print '老妈看到了 %s '% (lst_item)

def main():
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	for lst_iteam in lst:
		# print '老妈看到了 %s' % (lst_item)
		pass
		
	index = 0
	for lst_iteam in lst:
		# print '老妈看到了 %s '% (lst_item)
		# print '当前第 %d 个 ' %(index)
		index = index + 1
	for index, lst_item in enumerate(lst):
		# print '老妈看到了 %s '% (lst_item)
		# print '当前第 %d 个 ' %(index)
		pass
	print lst[0]
	
	print '--'
	
	lst2 = lst[0:5]
	print lst2
	for item in lst2:
		print item
	
	
if __name__ == '__main__':
	main()