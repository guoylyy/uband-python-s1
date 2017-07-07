#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小八

def main():
  good1 = '卷心菜'
  good2 = '罗马生菜'
  good3 = '有机番茄'
  good4 = '莳萝'
  good5 = '百里香'


  print '老妈看到了 %s '% (good1)
  print '老妈看到了 %s '% (good2)
  print '老妈看到了 %s '% (good3)
  print '老妈看到了 %s '% (good4)
  print '老妈看到了 %s '% (good5)

def main2():
  goods = '卷心菜，罗马生菜，有机番茄，莳萝，百里香'
  print '老妈看到了 %s' %(goods)

def main3():
  print '-------'
  lst = ['卷心菜', '罗马生菜', '有机番茄', '莳萝', '百里香'] #列表
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

if __name__ == '__main__':
  main()
  main2()
  main3()