#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

def main():
  lst = ['白菜 ','萝卜 ','西红柿 ','甲鱼 ','龙虾 ','生姜 ','白芍 ','西柚 ','牛肉 ','水饺 ']
  lst2 = lst[4:9] # 取第5个菜至第9个
  index = 0
  for lst_item in lst2:
  	if (index % 2) != 0:
  	
      print '老妈看到了 %s, 买了%d斤 '%（lst2[index],index +1）
  	  
  	else:
  	  print '老妈不买,继续逛 '
  	index = index +1 
  

   
  

if __name__ == '__main__':
	main()

  
