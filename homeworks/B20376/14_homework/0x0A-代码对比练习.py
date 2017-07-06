#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

def homework2():
	dictionary = {
          		 'abandon':'to give up to the control or influence of another person or agent',
         		 'abase':'to lower in rank, office, prestige, or esteem',
         		 'abash':'to destroy the self-possession or self-confidence of'
         		 }
	who = 'dad'

	tear_word = 'abandon'

	print ' %s 在看一本英文书' % (who)

	if not search('etiquette',who,dictionary):
		tear_mean = dictionary[tear_word]
		del dictionary[tear_word]
		print '%s 撕毁了 %s 的页面' %(who,tear_word)

	if search('abase',who,dictionary):
		dictionary[tear_word] = tear_mean
		print '%s 把 %s 的字典页又贴上了' %(who,tear_word)


def search(key,who,dictionary):
	if dictionary.has_key(key):
		print '%s 查询到了 %s : %s ' %(who,key,dictionary[key])
		return True
	else:
		print '%s 没有查询到 %s 的意思' %(who,key)
		return False

		
if __name__ == '__main__':
	homework2()