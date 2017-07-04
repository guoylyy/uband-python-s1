#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

def buy():
# 1. 老妈来到菜市场，从下标 0 开始遇到偶数下标就买,买的数量为下标 + 1 斤,遇到奇数下标就不买
    list = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
    for index, item in list:
        print '老妈来到菜市场，看到 %s' % (item)
        if index % 2 == 0:
            buy_amount = index + 1
            print '买了 %d 斤' % (buy_amount)
        else:
            print '没买'
    print '---------'
    
#  2. 完成后，用今天的学到的列表知识，加 3 个菜    
    list += ['冬瓜', '南瓜', '北瓜']
    #list.append('冬瓜')
    #del list[10]
    #list.remove('冬瓜')
    print len(list)
    print '---------'
   
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜  
    #list2 = list[5:10]
    for index, item in enumerate(list):
        if index in range(5,10):
            print '老妈来到菜市场，看到 %s' % (item)
            if index % 2 == 0:
                buy_amount = index + 1
                print '买了 %d 斤' % (buy_amount)
            else:
                print '没买'

if __name__ == '__main__':
  buy()