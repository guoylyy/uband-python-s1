#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

def main():
	dictionary = {
					'good':'of a favorable character of tendenc',
					'none':'not any such thing of person',
					'nice':'very beartiful'
					}
	try:
		print dictionary.value('magnificent')
	except BaseException as e:
		print '发生了错误 %s' %(e)

	

	try:
		print aa
	except NameError, e:
		print '发生了一个错误：%s'%(e)



if __name__ == '__main__':
	main()