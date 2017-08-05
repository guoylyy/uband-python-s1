#!/usr/bin/python
# -*- coding: utf-8 -*-

def buy(even_number2,amount,lst):
	if even_number2:
		for lst_item in lst:
			print '老妈来到菜市场'
			print '老妈看到%s，买了%d斤 '%(lst_item,amount)
		
def ignore():
	index=0
	even_number=False
	amount=0
	lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	for index,lst_item in enumerate(lst):
		if index%2==0:
			even_number=True
			amount=index+1
		else:
			print '老妈继续逛'
			print '老妈看到%s,不买'%(lst_item)
	return even_number,amount,lst

def main():
	even_number2,amount,lst=ignore()
	buy(even_number2,amount,lst)	
	



if __name__ == '__main__':
	main() 