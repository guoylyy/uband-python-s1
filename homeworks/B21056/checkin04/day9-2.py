#!/usr/bin/python
#-*- coding:utf-8 -*-
#@author:xxx

def main():
	print ' 老爸在看一本英文书，他旁边有一本只有3个单词解释的字典'
	dictionary={
				'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'
				}

	lst=['etiquette','abase']
	print lst.has_key(1) 
	for index,lst_item in enumerate(lst):
		#print index
		print '老爸要查单词”%s"'%(lst_item)
		if dictionary.has_key(lst_item):
			print '老爸很开心，了解到%s 的意思是 %s ,并把"abandon"加入到了字典'%(lst_item,dictionary['abase'])
			dictionary['abandon']='to give up to the control or influence of another person or agent'
			print '字典还有 %d 页'%(len(dictionary))
		else:
			print '没查到，老爸怒了，撕了"abandon" '
			del dictionary['abandon']
			print '字典还有 %d 页'%(len(dictionary))

if __name__ == '__main__':
	main()