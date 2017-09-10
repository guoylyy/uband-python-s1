#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: werewolf

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
# 1. 把老爸换成老妈，做的时候数一数改了几处代码 
#修改7处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
#修改2处/如果还要把abase粘回去的话再修改两处
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
#最前面加一个代码：lst_values=book.values()
#后面粘回去的时候输入：book['abase'] = lst_values[1]
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 需要把这段代码重复两遍
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  lst_keys=book.keys()
  lst_values=book.values()
  print '老妈在看一本英文书' 
  if book.has_key('abase'):
    print '老妈查到了 %s : %s'%(lst_keys[1],lst_values[1])
  if book.has_key('abash'):
    print '老妈查到了 %s : %s'%(lst_keys[2],lst_values[2])
  if not book.has_key('etiquette'): #没有查到
    print '老妈没有查到 %s 的意思' % ('etiquette') 

    #撕毁了abandon
    del book['abase']
    print '老妈撕毁了 %s 的页面' % ('abase')

    if book.has_key('abase'):
      print '老妈查到了 %s : %s' % ('abase', book['abase'])

      #老爸黏贴了代码
      book['abandon'] = 'to give up to the control or influence of another person or agent'
      print '老妈把 %s 的字典页又贴上了' % ('abandon')

    else:
      print '老妈没有查到 %s ' % ('abase') 
      book['abase'] = lst_values[1]
      print '老妈把 %s 的字典页又贴上了' % ('abase')
      print '字典里现在的单词有',book.keys()
  else:
    print '老妈查到了 %s '% ('etiquette')


if __name__ == '__main__':
  homework2()