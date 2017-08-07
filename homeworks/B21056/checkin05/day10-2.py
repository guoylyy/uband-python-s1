#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 实现了和 homework01 一样的功能
# 供你分析和对比
# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码---------------------共1处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码------------共1处
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = ' 老妈'
  tear_word = 'abandon' #可能会被撕毁的页的key
  list=['etiquette','abase','abash']


  print '%s在看一本英文书' % (who)
  for list_item in list:
    print '--------'
    if not search(list_item, book, who):
      tear_mean = book[tear_word]
      del book[tear_word]
      print '%s撕毁了 %s 的页面' % (who, tear_word)

      if search('abase', book, who):
        #老爸黏贴了代码
        book[tear_word] = tear_mean
        print '%s把 %s 的字典页又贴上了' % (who, tear_word)
  #for index,list_item  in enumerate(list):----------昨天写的，位置错了
  #  search(list_item,book,who)----------------------昨天写的，位置错了


def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()