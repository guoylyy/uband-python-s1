#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author:huafeng

# 1. 列表访问三种方法
# 2. 列表的几种运算
# 3. 做作业1
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
#   老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买,遇到奇数的下标就不买，买的数量为下标 + 1 斤
#   
def main ():
  #        0       1       2      3      4      5      6      7      8      9
  lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西瓜','牛肉','水饺'] # 列表
  print ('老妈来到了菜市场')

  print ('老妈看到了 %s '% (lst[0]))
  index = 0 
  for lst_item in lst :  #遍历

    if index % 2 == 0 :  #判断 指针为 奇偶数
      print ('老妈买了 %d 斤的 %s'% (index+1,lst[index])) 
      index = index + 1

    else :
      print ('老妈继续逛市场')
      index = index + 1
 # run function
if __name__ == '__main__':
   main()
   
