#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

def main():
	dictionary = {'good': 'of a favorable character or tendenc',
	'none':'not any such thing or person',
	'nice':'very beautiful'}

	print len(dictionary)
	print dictionary.keys()
	print dictionary.values()

	#是不是在
	print dictionary.has_key('good')
	print dictionary.has_key('bad')
# add
	dictionary['bad'] = "not very good"
	print dictionary
	print len(dictionary)

	#modify
	dictionary['bad'] = "falling to reach an acceptable stangard"
	print dictionary

	#delete
	del dictionary['bad']
	print dictionary
	print len(dictionary)

	# for
	print '---------------------'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有 bad 这个单词'


	for key in dictionary.keys():
		print key
		print dictionary[key]


if __name__ == '__main__':
  main()
