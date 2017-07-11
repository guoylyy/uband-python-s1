# -*- coding: utf-8 -*-
# @author: shuan

def main():
	week_overnight = [False, False, True, False, False]
	for index, is_overnight in enumerate(week_overnight):
		print '今天星期%d'%(index+1)
		try:
			overnight(is_overnight)
		except Exception,e:
			print '发生错误:%s'%(e)

def overnight(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
	    print '正常'

if __name__ == '__main__':
  main() 

def homework():
  lst= ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
 
  
  for index, lst_item in enumerate(lst):
  	try:
  	   index1(index,lst_item)
  	except Exception,e:
  		print '不买哼' 
  

def index1(index,lst_item):
    if index % 3 == 0:
  		print '老妈看到了%s，买了%d斤' % (lst_item, index+1)
  		index = index +1
    else:
	    raise Exception('no')
	    index=index+1

if __name__ == '__main__':
  homework()   


