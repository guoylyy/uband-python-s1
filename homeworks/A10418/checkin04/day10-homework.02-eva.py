#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = '老爸'
	tear_word = 'abandon'
	print '%s 在看一本英文书'%(who)

	if not search('etiquette',book,who):
  		tear_mean=book[tear_word]

  		del book[tear_word]
  		print '%s 撕毁了%s的页面'%(who,tear_word)

  		if search('abase',book,who):
  			book[tear_word]=tear_mean
  			print '%s把%s又粘上了'%(who,tear_word)

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s查询到%s:%s'%(who, key, dictionary[key])
		return True
	else:
		print '%s 没有查到%s 的意思'%(who,key)
		return False


def main01():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = '老妈'
	tear_word = 'abandon'
	print '%s 在看一本英文书'%(who)

	if not search('etiquette',book,who):
  		tear_mean=book[tear_word]

  		del book[tear_word]
  		print '%s 撕毁了%s的页面'%(who,tear_word)

  		if search('abase',book,who):
  			book[tear_word]=tear_mean
  			print '%s把%s又粘上了'%(who,tear_word)

def main02():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = '老妈'
	tear_word = 'abase'
	print '%s 在看一本英文书'%(who)

	if not search('etiquette',book,who):
  		tear_mean=book[tear_word]

  		del book[tear_word]
  		print '%s 撕毁了%s的页面'%(who,tear_word)

  		if search('abase',book,who):
  			book[tear_word]=tear_mean
  			print '%s把%s又粘上了'%(who,tear_word)	

def main04():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
	who = '老爸'
	tear_word = 'abandon'
	print '%s 在看一本英文书'%(who)

	if not search('etiquette',book,who):
  		tear_mean=book[tear_word]

  		del book[tear_word]
  		print '%s 撕毁了%s的页面'%(who,tear_word)

  		if search('abase',book,who):
  			book[tear_word]=tear_mean
  			print '%s 查到了%s'%(who,'abase')
  			print '%s把%s又粘上了'%(who,tear_word)
  			
  			if search('abase',book,who):
  				book[tear_word]=tear_mean
  				print '%s 查到了%s'%(who,'abase')

  				if search('abash',book,who):
  					book[tear_word]=tear_mean
  					print '%s 查到了%s'%(who,'abash')


if __name__ == '__main__':
	main04()

