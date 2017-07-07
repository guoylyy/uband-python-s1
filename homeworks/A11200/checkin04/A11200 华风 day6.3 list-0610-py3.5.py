#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author:huafeng
# 3. 做作业3
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺，加 3 个菜（丝瓜、冬瓜、辣椒）
#   老妈来到了菜市场，从下标 0 开始买菜，完成后，让老妈只逛第 5~9 个菜
#   遇到偶数的下标就买，遇到奇数的下标就不买， 买的数量为下标 + 1 斤

def main ():
  #        0       1       2      3      4      5      6      7      8      9
  lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西瓜','牛肉','水饺'] # 列表
  #lst2                                  0       1      2     3      4 
  lst.append ('丝瓜')
  lst.append ('冬瓜')
  lst.append ('辣椒')
  lst2 = lst[4:10]
  print ('老妈来到了菜市场')
  print ('老妈看到了 %s '% (lst2[0]))
  index = 0 
  for lst_item in lst2 :  #遍历
    if index % 2 == 0 :
      print ('老妈买了 %d 斤的 %s'% (index+1,lst2[index])) 
      index = index + 1
    else :
      print ('老妈继续逛市场')
      index = index + 1
if __name__ == '__main__':
   main()
   
