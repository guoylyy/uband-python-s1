#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
	index=0
	amount=0
	lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	lst.append('莴笋')
	lst.append('青菜')
	lst.append('鱼')
	lst2=lst[4:9]
	print '老妈来到菜市场 '
	for index,lst_item in enumerate(lst2):
		if index%2==0:
			amount=index+1+4
			print '老妈看到%s,买了%d斤 '%(lst[index+4],amount)
			print '老妈继续逛'
		else:
			print '老妈看到%s,不买 '%(lst[index+4])
			print '老妈继续逛'
	
		

if __name__ == '__main__':
	main()
	
	