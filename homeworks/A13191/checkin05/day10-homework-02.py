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

  print '%s在看一本英文书 ' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abase', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)
  print '-----'
  lst=['abase', 'abash']
  for lst_item in lst:
    search(lst_item, book, who)


def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()

#总结
#1. 对于有可能频繁更改的内容，最好用变量存储，这样可以避免大量的修改
#2. 对于频繁使用的功能，可以用一个函数实现，可以少写很多代码
#3. 写代码要注意考虑全面，各种可能出现的情况都要有对应的解决方法