#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

# 1. 把老爸换成老妈，做的时候数一数改了几处代码  【1处】
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码  【1处】
# 
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码  【none】

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老爸 '
  tear_word = 'abandon' #可能会被撕毁的页的key

  print '%s在看一本英文书' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abash', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)


def search(key, book, who):
  key = 'abase' #这里是因为在homework2里的第一个if语句运行时，需要先返回search模块里面做真值判断，
  #在这里abase赋值key之后，也就是此时etiquette被重新赋值成abase，也就是在search模块中的if语句为真，
  #直接查询到了abase，执行print '%s查询到了 %s:%s' % (who, key, book[key])，返回true到homework模块，
  #此时发现if not语句不成立，下面的代码均不执行，最终直接输出。

  if book.has_key(key):
    print '%s查询到了 %s:%s' % (who, key, book[key])
    return True
  else:
    print '%s没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  homework2()