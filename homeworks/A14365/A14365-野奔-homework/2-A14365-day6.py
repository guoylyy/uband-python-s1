#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: WangXiangChun

def guang(list):
    for index, food_name in enumerate(list):
      if index % 2 == 0 :
        index = index + 1
        print '老妈看见了%s,买了%d斤' %(food_name,index)
        print '老妈继续逛'
      else:
        print '老妈看见了%s,不买' %(food_name)
        print '老妈继续逛'

def homework():
  food1 = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  
  print '老妈来到了菜市场'
  guang(food1)
  print '---------'
  try:
    food2 = food1.extend(['黄瓜','丝瓜','青菜']) 
    guang(food2)
  except:
    print '发生错误'
  print '---------'

  food1[5:10]
  guang(food1)

if __name__ == '__main__':
    homework()