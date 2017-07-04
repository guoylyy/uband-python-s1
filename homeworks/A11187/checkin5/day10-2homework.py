#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui
 
def homework2():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": 'to lower in rank, office, prestige, or esteem',
			"abash": 'to destroy the self-possesion or self-confidence of'
			}
	who = 'father'
	tear_word = 'abandon'

	print '%s is reading an English book' % (who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print '%s tears the page of %s ' % (who, tear_word)

		if search('abase', book, who):
			book[tear_word] = tear_mean
			print '%s pastes the page of %s on the dictionary' % (who, tear_word)

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s finds out %s: %s' % (who, key, dictionary[key])
		return True
	else:
		print '%s does not find the meaning of %s' % (who,key)
		return False

if __name__ == '__main__':
	homework2()