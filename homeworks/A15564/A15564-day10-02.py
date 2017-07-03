#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

# 实现了和 homework01 一样的功能
# 供你分析和对比
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'  ##老爸 → 老妈
  tear_word = 'abase' #可能会被撕毁的页的key  ##abandon → abase

  print '%s在看一本英文书' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    search('abase', book, who)        ##个人认为此处不需要if语句，因不需要返回True或False
    #老爸黏贴了代码
    book[tear_word] = tear_mean
    print '%s把 %s 的字典页又贴上了' % (who, tear_word) 

  search('abase', book, who)  ## 搜abase
  search('abash', book, who)  ## 搜abash

def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s : %s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()
