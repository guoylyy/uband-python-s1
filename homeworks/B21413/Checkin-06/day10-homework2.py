#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 实现了和 homework01 一样的功能
# 供你分析和对比
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abase' #可能会被撕毁的页的key

  try:
    search(haha,book,who)
  except Exception,e:
    print '发生错误'
  else:
    print 'it looks good'


def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()