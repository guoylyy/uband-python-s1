#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: suancaiyu
#学习内容
#1，分支判断，列表，列表元素添加lst.append(),列表的分片lst[x:y] 注意分片的区间定义是对列表索引的的引用 包含索引x到y-1区间的元素
#2,编程实现：老妈从下标元素为0 开始买菜，遇到偶数的下标就买，奇数的不买 ,让老妈只看5~9个菜 


def homework():

  print '老妈来到菜市场'
#          0       1        2        3      4        5        6     7        8      9 
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']

  index = 0

  for lst_item in lst:

    if (index % 2) == 0:  
      
      print '老妈看到了%s,买了%d斤' % (lst_item, index +1)
    
    else:
      print '老妈看到了%s, 不买' % (lst_item)

    print '老妈继续逛'

    index = index +1



  print '------'

# 2 再加3个菜
def add_more():
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
  
  lst.append('菠菜')        #加的话，一次只能加一个。  三个用逗号隔开放一个括号里面失败了。
  lst.append('豆芽')
  lst.append('土豆')

  index = 0
  for lst_item in lst:
    print '妈妈看到了 %s' % (lst_item)
    index = index + 1
  

# 3 只逛第五到第九个菜
def selective():
  print '-------------'
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
  
  lst2 = lst[4:9]

  index = 0
  for lst_item in lst2:
    print '妈妈看到了 %s' % (lst_item)
  
    index = index + 1

def main():
  homework()
  add_more()
  selective()

if __name__ == '__main__':
  main()
