#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#把老爸换成老妈，一共改了七次代码，都是把老妈换成Mother
#把撕毁的页码换成'abase'，做的时候数一数改了六处代码
#:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词,一共有三处相同的代码


def homework2():
  book = {"abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }

  print 'Mother was reading an English book.'
  if book.has_key('abandon'): 
    print 'Mother查到 %s：%s' % ('abandon', book['abandon'])

  if book.has_key('abase'): 
    print 'Mother查到 %s：%s' % ('abase', book['abase'])

  if book.has_key('abash'): 
    print 'Mother查到 %s：%s' % ('abash', book['abash'])
  
if __name__ == '__main__':
  homework2()