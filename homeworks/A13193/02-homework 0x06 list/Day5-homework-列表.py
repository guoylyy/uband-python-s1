#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

def main(): #定义不同的变量 进行赋值
  good1 = '大白菜'
  good2 = '空心菜'
  good3 = '花菜'
  good4 = '生姜'
  good5 = '小龙虾'

  # ....... 省略掉 100 个
  good100 = '蚌壳'


  print '老妈看到了 %s '% (good1)
  print '老妈看到了 %s '% (good2)
  print '老妈看到了 %s '% (good3)
  print '老妈看到了 %s '% (good4)
  print '老妈看到了 %s '% (good5)

def main2(): 
  print '-------'
  goods = '大白菜，空心菜，花菜，生姜，小龙虾'
  print '老妈看到了 %s' %(goods)

def main3(): #数据的结构 lst = ['', '', '',] 只能是英文符号
  print '-------'
  lst = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾'] #列表 - 数组
  for lst_item in lst:  #遍历 for语句，解决一个变量能存储不同的数据 可以调用不同的数据
    print '老妈看到了 %s '% (lst_item)

if __name__ == '__main__':
  main()
  main2()
  main3()