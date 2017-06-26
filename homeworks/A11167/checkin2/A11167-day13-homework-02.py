#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: bettyyan

def print_list(lst):
  print '老妈来到菜市场，看到了 %s '% (lst)

def homework():
  print '老妈来到菜市场'
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
  for index, lst_item in enumerate(lst):
    print '老妈看到 %s ' %(lst_item)
    if index % 2 == 0: #遇到偶数的下标就买
      print '花了 %d 元' %(index +1)
  else:
    print '不买，继续逛'
try:
  for index, lst_item in enumerate(lst1):
    print '老妈看到 %s ' %(lst_item)
except NameError, e:
  print 'error:',e
 

if __name__ == '__main__':
  homework()