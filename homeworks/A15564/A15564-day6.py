#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

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

print '1.'

def odd(index):
    remainder = index %2
    if remainder == 0:
        return True

def homework():
    #          0         1         2         3         4          5            6             7           8         9
    lst = ['cabbage', 'radish', 'tomato', 'turtle', 'lobster', 'ginger', 'white peony', 'grapefruit', 'beef', 'dumplings']
    length = len(lst)
    print 'There are %s different kinds of food in the market:' %(length)
    for lst_item in lst:
        print lst_item
    print 'Here comes Mom to the market'

    # index = 0
    for index, lst_item in enumerate(lst):
        remainder = index % 2
        if odd(index):
            print 'Mom sees %s, and buys %d kg' %(lst_item, index+1)
            print 'And She goes on shopping'
        else:
            print 'Mom sees %s, but shows no interest' %(lst_item)
            print 'And She goes on shopping'
    print 'And she finally goes home'

if __name__ == '__main__':
    homework()

print '2.'

def add():
    #          0         1         2         3         4          5            6             7           8         9
    lst = ['cabbage', 'radish', 'tomato', 'turtle', 'lobster', 'ginger', 'white peony', 'grapefruit', 'beef', 'dumplings']
    lst.append('carrot')
    lst.append('fish')
    lst.append('chicken')
    length = len(lst)
    print 'There are now %s different kinds of food in the market:' %(length)
    for lst_item in lst:
        print lst_item

if __name__ == '__main__':
    add()

print '3.'

def odd(index):
    remainder = index %2
    if remainder == 0:
        return True

def fifth_to_nineth():
    #          0         1         2         3         4          5            6             7           8         9
    lst = ['cabbage', 'radish', 'tomato', 'turtle', 'lobster', 'ginger', 'white peony', 'grapefruit', 'beef', 'dumplings']
    length = len(lst)
    print 'There are %s different kinds of food in the market:' %(length)
    for lst_item in lst:
        print lst_item
    print 'Here comes Mom to the market'

    lst2 = lst[5:10]

    index = 5
    for lst_item in lst2:
        remainder = index % 2
        if odd(index):
            print 'Mom sees %s, and buys %d kg' %(lst_item, index+1)
            print 'And She goes on shopping'
        else:
            print 'Mom sees %s, but shows no interest' %(lst_item)
            print 'And She goes on shopping'
        index = index + 1
    print 'And she finally goes home'

if __name__ == '__main__':
    fifth_to_nineth()
