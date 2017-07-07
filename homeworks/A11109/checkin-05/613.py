#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: erhua

def main():
	dictionary = {
								'good':'of a favorable character or tendec',
								'none':'not any such thing or person',
								'nice':'very beautiful'
								}

	print len(dictionary)

	print dictionary.keys()

	print dictionary.values()

	print dictionary.has_key('good')

	print dictionary.has_key('bad')

	dictionary['bad'] = "not very good"

	dictionary['bad'] = "failing to reach an acceptable standard"
	print dictionary

	del dictionary['bad']
	print dictionary
	print len(dictionary)

	print '----'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有bad这个单词'
	print '-----'

	for key in dictionary.keys():
		print key
		print dictionary[key]

if __name__ == '__main__':
  main()