#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	dict={
		'abadon':'to give up to the control or influence of another person or agent',
		'abase' :'to lower in rank, office, prestige, or esteem',
		'abash' :'to destroy the self-possession or self-confidence of'
	}
	who='老妈'
	tear_word='abandon'
	if dict.has_key('etiquette'):
		print dict['etiquette']
	else:
		del dict['abadon']
		print '老爸怒了，撕掉\'abadon\'词页 '
		
	if dict.has_key('abase'):
		dict['abadon']='to give up to the control or influence of another person or agent'
		print '老爸很开心，把\'abadon\'词页加入词典 '
	
		try:
			if search(list(lst_item),dict,who):
				pass
			
			
		except Exception,e:
			print e

		
def search(key,dict,who):
	if dict.has_key(key):
		print '%s查询到%s:%s'%(who,key,dict[key])
		return True
	else:
		print '%s没有查到%s'%(who,key)
		return False
def list(lst_item):
	lst=['abase','abash']
	for lst_item in lst:
		return lst_item

if __name__ == '__main__':
	main()