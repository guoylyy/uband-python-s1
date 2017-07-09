#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

# 实现了和 homework01 一样的功能
# 供你分析和对比

def homework2():
  book = {
          "abandon":'to give up to the cintrol or influence of another person or agent',
          "abase":"to lower in rank,office,prestige,or esteem",
          "abash":"to destroy the self-possesion or self-confidence of"
        }
  who ='老爸 '
  tear_word = 'abandon'#可能被撕掉的页的key

  print '%s在看一本英文书 '%(who)
  if not search('etiquette',book,who):
    tear_mean=book[tear_word]

    del book[tear_word]
    print '%s撕毁了%s的页面 ' % (who,tear_word)

    if search('abase', book, who):
      #老爸黏贴了代码
      book[tear_word]=tear_mean
      print '%s 把 %s的字典页又贴上了 ' % (who,tear_word)

def search(key,dictionary,who):
  if dictionary.has_key(key):
    print '%s查询到了 %s:%S ' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s的意思 ' % (who,key)
    return False

if __name__ == '__main__':
  homework2()


