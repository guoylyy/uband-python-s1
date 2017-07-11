#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小白

def main():
  print '老妈来到菜市场'


  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
  lst.append('山药')
  lst.append('芥蓝')
  lst.append('羊肉')
  
  lst2 = lst[4:10]
  for index, lst_item in enumerate(lst2):
    if index % 2 == 0:
      buy_amount = index + 4
      print  '老妈看到了%s, 买了 %d 斤'%(lst_item, buy_amount)
    else:
      print '老妈继续逛,看到%s, 不买'%(lst_item) 


if __name__ == '__main__':
  main()

