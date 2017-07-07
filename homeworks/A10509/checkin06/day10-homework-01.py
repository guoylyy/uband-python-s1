#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老妈在看一本英文书'
  if not book.has_key('etiquette'): #没有查到
    print '老妈没有查到 %s 的意思' % ('etiquette')
    tear_mean = book["abandon"]
    #撕毁了abandon
    del book['abase']
    print '老妈撕毁了 %s 的页面' % ('abase')

    if book.has_key('abase'):
      print '老妈查到了 %s : %s' % ('abase', book['abase'])

      #老爸黏贴了代码
      book["abandon"] = tear_mean
      print '老妈把 %s 的字典页又贴上了' % ('abase')

    else:
      print '老妈没有查到 %s ' % (abase) 
  else:
    print '老妈查到了 %s '% ('etiquette')


def cha():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
    who = 'baba'
    tear_word = 'abandon'
    
    if not search("etiquette", book, who):
    	tear_mean = book[tear_word]
    	del book[tear_word]
    	print '%s撕毁了 %s 的页面' % (who, tear_word)

    	if search("abase", book, who):
    		book[tear_word] = tear_mean
    		print '%s把 %s 的字典页又贴上了' % (who, tear_word)

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print "%s 查到%s意思是%s" %(who, key, dictionary[key])
		return True
	else:
		print "%s没有查到%s" %(who, key)
		return False

if __name__ == '__main__':
	cha()