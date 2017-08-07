#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abandon'

  print_dictionary(book)

  print '%s在看一本字典'% (who)
  if not search('etiquetee', book, who):

  	tear_mean = book[tear_word]
  	del book[tear_word]
  	print '%s撕掉了含有%s的那一页' % (who, tear_word)

  	if search('abase', book, who):
  		book[tear_word] = tear_mean
  		print '%s把%s那一页又粘回去了'% (who,tear_word)

 

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s查询到了%s: %s'% (who, key, dictionary[key])
		return True
	else:
		print '%s没有查询到了%s'% (who, key)
		return False

def print_dictionary(dictionary):
	num = len(dictionary)
	lst = [None]*num
	for key in dictionary.keys():
		print '书里有%s:%s'% (key, dictionary[key])



if __name__ == '__main__':
  homework2()