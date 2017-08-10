#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#把老爸换成老妈，一共改了七次代码，都是把老妈换成Mother
#把撕毁的页码换成'abase'，做的时候数一数改了六处代码

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print 'Mother was reading an English book.'
  if not book.has_key('etiquette'): #没有查到
    print 'Mother没有查到 %s 的意思' % ('etiquette')

    #撕毁了abandon
    del book['abase']
    print 'Mother撕毁了 %s 的页面' % ('abase')

    if book.has_key('abase'):
      print 'Mother查到了 %s : %s' % ('abase', book['abase'])

     
    else:
      print 'Mother没有查到abase这个单词 '
      #老爸黏贴了代码
      book['abase'] = 'to lower in rank, office, prestige, or esteem'
      print 'Mother把 %s 的字典页又贴上了' % ('abase')

  else:
    print 'Mother查到了 %s '% ('etiquette')  #不执行

if __name__ == '__main__':
  homework2()