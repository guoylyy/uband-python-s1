#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

#def main():
     #   1      2         3
	#lst=['杨洋','片寄凉太','张一山']
	#index=1
	#index=index+1
	#for index,lst_item in enumerate(lst):
		#print '%s是我的第%d个偶像' %(lst_item,index+1) 
		#index从0开始计数是默认的。把括号里面改成index+1 或者使用切片 [1:]
	
#if __name__ == '__main__':
	#main()
	#print '片寄老妈来到了菜市场'
	#lst[0,2,4,6,8]= True

#       0     1      2        3     4      5      6      7      8       9
	#lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺'] #列表
	#偶数下标（买）：0，2，4，6，8 buy_amount = index + 1
	#奇数下标（不买）：1，3，5，7，9，


#def buybuybuy(lst):
	#index=0
	#buy_amount=index+1
	#'白菜','西红柿','龙虾','白芍','牛肉'=True
	#if True:
		#print '买了%s%d斤,继续逛'%(lst_item,buy_amount)
	#else:
		#print '没买，继续逛'

#def come_to_market():
	#print '片寄老妈来到了菜市场'
	#       0     1      2        3     4      5      6      7      8       9
	#lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺'] #列表



#def print_list(lst):
	#for lst_item in lst:
		#print '老妈看到了%s' %(lst_item)

	

#def main():
	#lst = come_to_market()
	#print_list(lst)
	#buybuybuy(lst)

#if __name__ == '__main__':
	#main()

#-------------------------------天呐，上面全是错的，还是脑子不清醒。。。。呜呜呜。。。老师说非常简单。。。心痛死了
#错误原因：1.我不知道index % 2 ==0是什么东西 2.我把东西过于复杂化了。3.脑子抽了吧可能。。。

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

#这个下面的还是最后看老师讲评视频里才做出来的
#这里面后来加了三个菜
#然后让老妈只逛5-9个菜

def main():
	print '老妈来到菜市场'
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	lst.append('芹菜')   #这里之前犯了一个错误，千万不能写成 lst.append ('芹菜'，'盐酥鸡','臭豆腐')
	lst.append('盐酥鸡')
	lst.append('臭豆腐')
	lst2=lst[5:10] #切片 分片完赋值给lst2,就代表lst2是一个只有5个元素的新数组。
	
	index=0
	for lst_item in lst2:
		if index % 2 ==0:
			print '老妈看到了%s,买了%d斤'%(lst_item, index+1)
		else:
			print '老妈看到了%s,没买'%(lst_item)
		index=index+1 #必须要加，不加不行！！！

		print '老妈继续逛'

		
		
if __name__ == '__main__':
	main()






		
		



	

