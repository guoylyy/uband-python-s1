#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里
# 
# 老爸把字典翻了一遍
#   - 看到%s（单词）:%s(意思)
# 
# 第二个作业我已经做完，先不要看第二个版本

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码  7
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码 2
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码 8行(不知道是查到了一个词再查两个，还是直接查两个，所以可能算错了)
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老妈在看一本英文书'
  if not book.has_key('etiquette'): #没有查到
    print '老妈没有查到 %s 的意思' % ('etiquette')

    #撕毁了abandon
    bookdel={'abandon':book['abandon']}
    del book['abandon']
    print '老妈撕毁了 %s 的页面' % ('abase')

    if book.has_key('abase'):
      print '老妈查到了 %s : %s' % ('abase', book['abase'])

      #老爸黏贴了代码
      # book['abandon'] = 'to give up to the control or influence of another person or agent'

      if book.has_key('abash') and book.has_key('abase'):
        print '老妈查到了 %s : %s,%s : %s' % ('abash', book['abash'],'abase', book['abase'])
        book['abandon']=bookdel['abandon']
        print'老妈很开心，又把%s加入字典里'%('abandon')
      #老爸黏贴了代码
      # book['abandon'] = 'to give up to the control or influence of another person or agent'

      else:
        print '老妈没有查到 %s ' % ('abash,abase') 
    else:
      print '老妈没有查到 %s ' % ('abase')
  else:
    print '老妈查到了 %s '% ('etiquette')


if __name__ == '__main__':
  homework2()