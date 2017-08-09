#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
def main():
	# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
	
	book={
				'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem ',
				'abash':'to destroy the self-possession or self-confidence of'
				}
	who='dad'
	tear_word='abandon'#可能会被撕毁的Key
	print'%s is looking at an English book, he has a book which only has the explanation of three word.'%(who)
	if not search('etiquette',book,who):
		tear_mean=book[tear_word]
		del book[tear_word]
		print'%s tear %s '%(who,tear_word)

		if search('abase',book,who):
			book[tear_word]=tear_mean
			print'%s fix %s'%(who,tear_word)
		lst=['abase','abash']
		for lst_item in lst:
			print search(lst_item,book,who)
			if search(lst_item,book,who):
				pass
def search(key,dictionary,who):
	if dictionary.has_key(key):
		print'%s find %s:%s'%(who,key,dictionary[key])
		return True
	else:
		print'%s didnot find %s'%(who,key)
		return False

if __name__ == '__main__':
  main()