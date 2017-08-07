#!usr/bin/python
#-*- coding: utf-8 -*-
#@author: Karen
# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
#    
# 【提示】：
#   输出结果可能为
#   ‘老妈来到菜市场
#    老妈看到白菜，买了 1 斤
#    老妈继续逛
#    老妈看到xxx, 不买
#    老妈继续逛
#    ...
#   '
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def add(lst):
	lst.append('鸡爪')
	lst.append('青椒')
	lst.append('西瓜')	

def odd_even(index):
	is_even=index % 2 #取模，返回余数，余数为 1-奇数，0-偶数
	if is_even == 0:
		return True
	else:
		return False

def print_list(lst):
	print ' 老妈来到菜市场'
	is_even=False
	for index,lst_item in enumerate(lst):
		is_even= odd_even(index)
		if is_even:
			print '老妈看到了%s，买了%d斤'%(lst_item,index+1)
		else:
			print '老妈看到了%s,不买'%(lst_item)
		print '老妈继续逛'

def main():
#			  0		1		2	   3	  4  	5		6		7	   8	 9 
#买几斤		  1		不买	3斤   不买	  5斤	不买	7斤	  不买    9斤	不买
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	
#作业2：增加3个菜
	add(lst)
#作业3：切片
	#lst2=lst[5:10]
	#迭代访问
	print_list(lst)
	#print_list(lst2)

if __name__ == '__main__':
	main()
	