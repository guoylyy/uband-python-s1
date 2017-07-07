#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: erhua

def main():
  dictionary = {
  							'abandon':'to give up to the control or influence of another person or agent',
  							'abase':'to lower in rank, office, prestige, or esteem',
  							'abash':'to destroy the self-possession or self-confidence of'
  							}

  print "老爸先查了一个单词'etiquette'"
  if  dictionary.has_key('etiquette') : #
  	print dictionary['etiqueette']
  else:
  	print "没有查到,老爸把'abandon'一页的单词撕掉了"

  del dictionary['abandon']
  print dictionary

  print "然后老爸又查了一个单词'abase', 得到了解释"
  if dictionary.has_key('abase'):
  	print dictionary['abase']
  	print "老爸很开心, 又把'abandon'加入词典"
  else:
  	print '没有abase这个单词'
  							
  dictionary['abandon'] = "to give up to the control or influence of another person or agent"
  print dictionary


if __name__ == '__main__':
  main()

  