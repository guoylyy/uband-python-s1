#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

def main():
	dictionary = {
					'good':'of a favorable character',
					'none':'not any such thing',
					'nice':'very beatuiful'
				}
	print len(dictionary)

	print dictionary.keys()

	print dictionary.values() #获取相关列表

	print dictionary.has_key('good')
	print dictionary.has_key('zoo')

	dictionary['bad'] = 'not good'

	print dictionary

	del dictionary['bad']

	print dictionary

	print '-------'

	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '字典中没有'


	for key in dictionary.keys():
		print key
		print dictionary[key]



if __name__ == '__main__':
	main()