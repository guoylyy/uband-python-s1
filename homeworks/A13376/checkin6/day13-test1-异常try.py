#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():

  tuple = ( False,True,False,False)
  print tuple

  print '-----try------'
  for index,is_overfat in enumerate(tuple):
  	print '第%s个人' % (index + 1)
  	
  	try:
  		overfat_check(is_overfat)
  	except Exception as e:
  		print '%s' %(e)
  	else:
  		print '臣复议'

def overfat_check(is_overfat):
	if is_overfat:
		raise Exception('查无此人')
	else:
		print '你太胖了'
# run function
if __name__ == '__main__':
  main()