#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

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
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  book = {
           "abandon":'to give up to the control or influence of anther person or agent',
           "abase":"to lower in rank, office, prestige, or esteem",
           "abash":"to destroy the self-prossession or self-cofidence of"
           }
  print '老爸在看一本英文书 '
  if not book.has_key('etiquette'): #如果没有etiquette 
    print'老爸没查到 %s 的意思 '%('etiquette')
    #撕掉abandon
    del book['abandon'] # 删了abondon
    print '老爸撕毁了%s的意思 '%('abandon')

    if book.has_key('abase'): #如果没有etiquette ,但有 abase
      print '老爸查到了 %s : %s ' %('abase',book['abase']) 
      #老爸贴上代码
      book['abandon'] = 'to give up the control or influence of another person or agent'
      print '老爸把%s 的字典页又贴上了 '%('abandon')

    else: #如果没有etiquette ,也没有 abase
      print '老爸没有查到 %s '%('abase')
  else: #如果有etiquette 
    print '老爸查到了%s ' %('etiquette')
if __name__ == '__main__':
  homework2 ()

# 1. 把老爸换成老妈，做的时候数一数改了几处代码
def homework2():
  print'----------------'
  book = {
           "abandon":'to give up to the control or influence of anther person or agent',
           "abase":"to lower in rank, office, prestige, or esteem",
           "abash":"to destroy the self-prossession or self-cofidence of"
           }
  print '老妈在看一本英文书 '# 第一处
  if not book.has_key('etiquette'): #如果没有etiquette 
    print'老妈没查到 %s 的意思 '%('etiquette')# 第二处
    #撕掉abandon
    del book['abandon'] # 删了abondon
    print '老妈撕毁了%s的意思 '%('abandon') # 第三处
 
    if book.has_key('abase'): #如果没有etiquette ,但有 abase
      print '老妈查到了 %s : %s ' %('abase',book['abase']) # 第四处
      #老爸贴上代码
      book['abandon'] = 'to give up the control or influence of another person or agent'
      print '老妈把%s 的字典页又贴上了 '%('abandon')# 第五处

    else: #如果没有etiquette ,也没有 abase
      print '老妈没有查到 %s '%('abase') # 第六处
  else: #如果有etiquette 
    print '老妈查到了%s ' %('etiquette') # 第七处
if __name__ == '__main__':
  homework2 ()


#2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
def homework2():
  print'----------------'
  book = {
           "abandon":'to give up to the control or influence of anther person or agent',
           "abase":"to lower in rank, office, prestige, or esteem",
           "abash":"to destroy the self-prossession or self-cofidence of"
           }
  print '老妈在看一本英文书 '
  if not book.has_key('etiquette'): #如果没有etiquette 
    print'老妈没查到 %s 的意思 '%('etiquette')
    #撕掉abase
    del book['abase'] # 删了abase 第一处
    print '老妈撕毁了%s的意思 '%('abase') #第二处
 
    if book.has_key('abase'): #如果没有etiquette ,但有 abase
      print '老妈查到了 %s : %s ' %('abase',book['abase']) 
      #老爸贴上代码
      book['abase'] = 'to lower in rank, office, prestige, or esteem'#第三处
      print '老妈把%s 的字典页又贴上了 '%('abase')# 第四处

    else: #如果没有etiquette ,也没有 abase
      print '老妈没有查到 %s ' % ('abase') 
  else: #如果有etiquette 
    print '老妈查到了%s ' %('etiquette') 
if __name__ == '__main__':
  homework2 ()
 
 # 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意(不知道怎么做)
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
def homework2():
  print'-----------------------'
  book = {
           "abandon":'to give up to the control or influence of anther person or agent',
           "abase":"to lower in rank, office, prestige, or esteem",
           "abash":"to destroy the self-prossession or self-cofidence of"
           }
  print '老爸在看一本英文书 '
  if not book.has_key('etiquette'): #如果没有etiquette 
    print'老爸没查到 %s 的意思 '%('etiquette')
    #撕掉abandon
    del book['abandon'] # 删了abondon
    print '老爸撕毁了%s的意思 '%('abandon')

    if book.has_key('abase'): #如果没有etiquette ,但有 abase
      print '老爸查到了 %s : %s ' %('abase',book['abase']) 
      #老爸贴上代码
      book['abandon'] = 'to give up the control or influence of another person or agent'
      print '老爸把%s 的字典页又贴上了 '%('abandon')

    else: #如果没有etiquette ,也没有 abase
      print '老爸没有查到 %s '%('abase')
  else: #如果有etiquette 
    print '老爸查到了%s : %s' %('etiquette',book['etiquette'] )
if __name__ == '__main__':
  homework2 ()
 

def search():
  book = {
           "abandon":'to give up to the control or influence of anther person or agent',
           "abase":"to lower in rank, office, prestige, or esteem",
           "abash":"to destroy the self-prossession or self-cofidence of"
           }
  print '老爸搜索到 %s 和%s '% ('abase','abash')


if __name__ == '__main__':
  search()

