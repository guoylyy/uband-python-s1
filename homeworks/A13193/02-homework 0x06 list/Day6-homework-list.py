#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

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
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

def homework():
  #         0       1       2         3       4      5        6       7       8       9
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺'] #列表
  # 循环访问
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

  # 记录下标
  print '======='
  index = 0
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)    
    print '当前第 %d 个' %(index)
    index = index + 1

  # 迭代访问
  print '======='
  for index,lst_item in enumerate(lst):
    print '老妈看到了 %s '% (lst_item)    
    print '当前第 %d 个' %(index)

  #从下标0开始，遇偶数买菜，买的数量为下标+1斤，遇奇数不买菜
  print '======='
  index = 0
  for lst_item in lst:  #遍历
    if index % 2 == 0:
    	print '老妈看到了 %s, 她买了 %d 斤 '% (lst_item, index + 1)
    else:
    	print '老妈看到了 %s, 并没有买 '% (lst_item)
    index = index + 1


  #取值
  #print '======='
  #print lst[0]

  #长度
  #print '======='
  #print len(lst)
  
  #加三个菜：山药、黄鳝、西兰花
  print '======='
  lst.append('山药')
  lst.append('黄鳝')
  lst.append('西兰花')
  print_list(lst)
  print len(lst)


  #切片 老妈只逛第5~9个菜
  print '======='
  lst2 = lst[5:10] # 5,6,7,8,9
  print_list(lst2)







if __name__ == '__main__':
  homework()
