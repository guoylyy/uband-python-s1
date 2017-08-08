#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Masur

#sample code
# def print_list(lst):
# 	for lst_item in lst:
# 		print '老妈看到了 %s '%(lst_item)
# def main():
# 	lst=['大白菜','空心菜','花菜','生姜','小龙虾']
# 	print '---循环访问---'
# 	for lst_item in lst:
# 		print '老妈看到了 %s '%(lst_item)
# 	print '---记录下标---'
# 	index=0
# 	for lst_item in lst:
# 		print '老妈看到了 %s '%(lst_item)
# 		print '当前第 %d 个'%(index)
# 		index=index+1
# 	print '---迭代访问---'
# 	for index,lst_item in enumerate(lst):
# 		print '老妈看到了 %s '%(lst_item)
# 		print '当前第 %d 个'%(index)
# 	# 取值
# 	print lst[0]
# 	# 长度
# 	print len(lst)
# 	# 加
# 	lst.append('白芍')
# 	print_list(lst)
# 	print'--------'
# 	# 删除
# 	del lst[0]
# 	print_list(lst)
# 	# 切片
# 	lst2=lst[0:3]
# 	print_list(lst2)
# 	# 2-4
# 	lst3=lst[2:5]
# 	print_list(lst3)

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
def print_list(lst):
	for lst_item in lst:
		print '老妈看到了 %s'%(lst_item)
def homework():
	# Q1
  lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  print '老妈来到菜市场'
  index=0
  for lst_item in lst:
  	if index % 2 ==0:
  		print '老妈看到%s,买了%d斤'%(lst_item,index+1)
  	else:
  		print '老妈看到%s,不买'%(lst_item)
  	print '老妈继续逛'
  	index=index+1
  #Q2
  print '---Q2---'
  lst.append('西瓜')
  lst.append('南瓜')
  lst.append('冬瓜')
  print_list(lst)

  # Q3
  print '---Q3---'
  lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  lst2=lst[5:10]
  print_list(lst2)

  try:
    print lst[20]
  except Exception, e:
    print 'error: %s' %(e) 
  
  

if __name__ == '__main__':
	# main()
    homework()