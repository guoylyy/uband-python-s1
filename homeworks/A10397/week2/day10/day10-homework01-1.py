#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码 【7处】
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码  【2处】
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意 
     #【设置两个代码块 用return返回值】
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码 【2处】

def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老爸在看一本英文书 '
  if not book.has_key('etiquette'): #没有查到
    print '老爸没有查到 %s 的意思' % ('etiquette')

    #撕毁了abandon
    del book['abandon']
    print '老爸撕毁了 %s 的页面' % ('abandon')

    if book.has_key('abase'):
      print '老爸查到了 %s : %s' % ('abase', book['abase'])

      #老爸黏贴了代码
      book['abandon'] = 'to give up to the control or influence of another person or agent'
      print '老爸把 %s 的字典页又贴上了' % ('abandon')

    else:
      print '老爸没有查到 %s ' % ('abase') 
  else:
    print '老爸查到了 %s '% ('etiquette')

    #作业4 【重复打印代码 2处】
  if book.has_key('abase'):
  	print '老爸查到了 %s ：%s' %('abase', book['abase'])
  else:
  	print '老爸没有查到 %s 的意思' %('abase')

  if book.has_key('abash'):
  	print '老爸查到了 %s ：%s' %('abash', book['abash'])
  else:
  	print '老爸没有查到 %s 的意思' %('abash')  





if __name__ == '__main__':
  homework2()