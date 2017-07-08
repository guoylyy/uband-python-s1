
# -*- coding: utf-8 -*-
# @author: shuan


# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
def homework():
  lst= ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  index = 0
  
  for lst_item in lst:
  	if index % 2 == 0:
  		print '老妈看到了%s，买了%d斤' % (lst_item, index+1)
  		index = index +1
  	else:
  		print '老妈看到了%s，不买' % (lst_item)
  		index = index+1

if __name__ == '__main__':
  homework()   

#  2. 完成后，用今天的学到的列表知识，加 3 个菜
def homework2():
  lst= ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  index = 0
  lst.append('土豆')
  lst.append('大葱')
  lst.append('大蒜')
  for lst_item in lst:
  	print lst_item
  return lst

#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def homework3():
  lst2 = lst[4:9]
  for index,lst2_item in enumerate(lst2):
  	print '老妈看到了%s，买了%d斤' % (lst2_item, index+1)

if __name__ == '__main__':
  lst= homework2()
  homework3()