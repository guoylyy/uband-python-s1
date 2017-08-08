#!/usr/bin/python
# -*- coding: utf-8 -*-

def main1():
	dictionary={
				'good':'of a favorable character or tendenc',
				'none':'not any such thing or person',
				'nice':'very beautiful'
				}

	#获取长度
	print len(dictionary)

	#获取keys
	print dictionary.keys()

	#获取values
	print dictionary.values()

	#是不是在字典中
	print dictionary.has_key('good')

	#add
	dictionary['bad']='not very good'

	#modify
	dictionary['bad']='failing to reach the standard'

	#delete
	del dictionary['bad']

	#get value
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print '没有 bad 这个词'

	#iterator

	for key in dictionary.keys():
		print key
		print dictionary[key]
	

def main2():
	dictionary ={'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'}

	print 'dad read an english book. \
			he had a dictionary aside\
			but the dictionary only has three words'
	for key in dictionary.keys():
		print key
		print dictionary[key]

	print 'dad looked up “etiquette” in the dictionary first'

	if dictionary.has_key('etiquette'):
		pass
	else:
		print 'he did not find it and felt angry, so he tore the page of %s '%('abondon')

	
	print 'then, he looked “abase” in the dictionary'
	if dictionary.has_key('abase'):
		print 'dad found it and was happy, so he added the page of %s into the dictionary'%('abondon')
	else:
		pass



if __name__ == '__main__':
	main2()






