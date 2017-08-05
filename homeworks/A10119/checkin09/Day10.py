#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan


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
# 1. 把老爸换成老妈，做的时候数一数改了几处代码——8处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码——4处
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码——最多4处
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老爸在看一本英文书 '
  if not book.has_key('etiquette'): #第一次尝试用not
  	print '老爸没有查到 %s 的意思' % ('etiquette')

  	del book['abandon']
  	print '老爸撕毁了 %s 的页面' % ('abandon')

  	if book.has_key('abase'):
  		print '老爸查到了 %s : %s' % ('abase', book['abase'])

  		book['abandon'] = 'to give up to the control or influence of another person or agent'
  		print '老爸把 %s 的字典页又贴上了 ' % ('abandon')
  	else:
  		print '老爸没有查到 %s '% ('abase')
  else:
  	print '老爸查到了 %s ' % ('etiquette')

  if book.has_key('abase'):
  	print '老爸查到了 %s : %s' % ('abase', book['abase'])
  if book.has_key('abash'):
  	print '老爸查到了 %s : %s' % ('abash', book['abash'])

  print '老爸把字典翻了一遍 '
  for key in book.keys():
  	print '看到 %s : %s' % (key, book[key])
  	

if __name__ == '__main__':
  homework2()


  #总结
  #1.原来代码可以写的这么简洁而不啰嗦，本以为是有用到新的语句才能实现
  #2.如果想在后期随时改动变量，就在一开始的时候定义标签，
     #在没有这样做的时候，重复代码的地方非常多，改动起来也很麻烦
  #3.if not代表如果不是xxx，则执行下面的命令
  #4.自己每次开始写的时候都这么啰嗦.....伤感，感觉文科生的思维就是网状的...
