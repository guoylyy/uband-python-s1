#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小白

def main():
  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释'

  dictionary = {
                'abandon':'to give up to the control or influence of another person or agent',
                'abase': 'to lower in rank, office, prestige, or esteem',
                'abash': 'to destory the self-possession or self-confidence of'
               }
  for key in dictionary.keys():
    print key
    print dictionary[key]

  print "老爸先查了一个单词 'etiquette'"
  if dictionary.has_key('etiquette'):
    print dictionary['etiquette']
  else:
    del dictionary['abandon'] 
    print '老爸怒了,撕毁了%s 的那页' % ('abandon')

  print "老爸又查了一个单词'abase'"
  if dictionary.has_key('abase'):
    print key
    print dictionary['abase']
    print "老爸很开心，又把 'abandon' 加入到了字典里"
    dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
  else:
    print '老爸没有查到单词'



if __name__ == '__main__':
  main()