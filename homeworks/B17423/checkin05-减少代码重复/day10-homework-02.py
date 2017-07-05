#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

# 实现了和 homework01 一样的功能
# 供你分析和对比
# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码
##### 1处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
##### 1处

# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
######  不需要添加打印代码，调用search函数

#总结：
##### 昨天做作业的时候已经写了search函数，但是没有考虑到添加变量who和tear_word, tear_mean减少代码的重复
##### 写代码之初就觉得单一职责原则和减少代码重复能很好的精简代码，也能让代码思路更清晰，便于之后的修正
##### 在写代码的时候也经常会考虑这两个原则，但还是考虑的不够全面吧，shushu给了很好的提醒~以后应该多加注意。
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abandon' #可能会被撕毁的页的key

  print ('%s在看一本英文书' % who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print ('%s撕毁了 %s 的页面' % (who, tear_word))

    if search('abase', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print ('%s把 %s 的字典页又贴上了' % (who, tear_word))

    #question 4
    search('abase', book, who)
    search('abash', book, who)


def search(key, dictionary, who):
  if key in dictionary:
    print ('%s 查询到了 %s:%s' % (who, key, dictionary[key]))
    return True
  else:
    print ('%s 没有查询到 %s 的意思' %(who, key))
    return False


if __name__ == '__main__':
  homework2()