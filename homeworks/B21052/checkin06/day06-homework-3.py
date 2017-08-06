#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel


def main():

  #       0      1       2      3       4     5      6      7      8     9
  lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']

  lst.append('猪肉')
  lst.append('豆角')
  lst.append('黄瓜')

  lst2 = lst[5:10] 
  
  print 'One day, my mum came to the vegetable market.'
 
  for index,lst_item in enumerate(lst2):
      if index % 2 == 0:
        print 'She saw %s,and bought %dkg;'% (lst_item,index + 1)    
      else:
        print 'She went on shopping'
        print 'She saw %s, but didnot buy them and walked away.'% (lst_item)   

if __name__ == '__main__':
  main()