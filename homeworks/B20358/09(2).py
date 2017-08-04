#!/usr/bin/python
# -*- coding:utf-8 -*-
#author: Anna

def main():
	dictionary = {
	              'abandon':'to give up to the control or influence of another person or agent',
                  'abase':'to lower in rank, office, prestige, or esteem',
                  'abash':'to destroy the self-possession or self-confidence of'
	             }
	print dictionary

	if dictionary.has_key('etiquette') == False:
		print '老爸没查到 etiquette , 老爸怒了, 把 abandon 一页的单词撕掉了'
	del dictionary['abandon']
	print dictionary

	if dictionary.has_key('abase') == True:
		print '老爸得到了 abase 的解释是 %s' % (dictionary['abase'])
		
		print '老爸很开心, 把 abandon 加入到了字典里'

	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print dictionary




if __name__ == '__main__':
	main()