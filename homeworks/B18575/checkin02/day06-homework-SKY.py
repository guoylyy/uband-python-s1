#!usr/bin/python
# -*- coding:utf-8 -*-
# @author:SKY
def homework():
	list_item=['白菜','萝卜','红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	print '老妈来到了菜市场'
	buybuybuy(list_item)
	#列表中，添加三个菜
	list_item.append('土豆')
	list_item.append('豆角')
	list_item.append('羊肉')
	#听说来了新菜，老妈又来逛菜市场
	print '菜市场来了新菜，老妈又来逛菜市场'
	buybuybuy(list_item)

	#老妈今天决定不逛这么多了，选几个菜看看
	print '老妈今天没空，决定选几个菜看看'
	lst_item=list_item[4:9]
	buybuybuy(lst_item)
#老妈逛菜市场
def buybuybuy(list_item):
	#取出列表中的下标和数据
	for index,item in enumerate(list_item):
		#判断下标，是否买菜，偶数下标买，奇数下标不买
		if(index%2==0):
			print '老妈看到了 %s,买了 %d 斤' %(item,index+1)
		else:
			print '老妈看到了 %s,没买' % (item)
		if(index==len(list_item)-1):
			print '老妈逛完了,回家了'
		else:
			print '老妈继续逛'
if __name__ == '__main__':
	homework()