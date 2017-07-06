#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

def main():
	dictionary = {
	              'thesaurus' : 'reference book in which words with similar meanings are grouped together',
	              'storehouse' : 'a building in which things, usually food, are stored',
	              'kind' : 'one of the types or sorts of that thing'
	             }
	print len(dictionary)#
	print dictionary.keys()#
	print dictionary.values()#
	print dictionary.has_key('thesaurus')#
	print dictionary.has_key('warehouse')#
	
	dictionary['warehouse'] = "a building"#
	print dictionary
	print len(dictionary)

	dictionary['warehouse'] = "a large building where raw materials or manufactured goods are stored until they are exported to other countries or distributed to shops to be sold"#
	print dictionary

	del dictionary['warehouse']
	print dictionary
	print len(dictionary)

	print '-----'
	print dictionary{}
	if  dictionary.has_key['warehouse']:
		print dictionary['warehouse']
	else:
		print'没有warehouse这个单词'

	print '-----'

	for key in dictionary.keys():
		print key
		print dictionary[key]


if __name__ == '__main__':
	main()