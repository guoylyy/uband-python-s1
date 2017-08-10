#!/usr/bin/python
# -*- coding: UTF-8 -*-  
#author fangcheng
def main():
	week_overnight = [False, False, True, False, False] #周一到周五的情况

	for index,is_overnight in enumerate(week_overnight):
	  print '今天是星期%d' % (index + 1)
	  try :
	    overnight_check(is_overnight)
	  except Exception,e:
	  	print '发生错误:%s'%(e)
	  else :
	  	#当不发生错误时候的情况
	  	print '附带脚本'

def overnight_check(is_overnight):
	if is_overnight:
	  raise Exception('离婚')
	else:
	  print '正常'

if __name__ == '__main__':
  main()