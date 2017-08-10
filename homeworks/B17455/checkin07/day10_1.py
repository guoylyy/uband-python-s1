#!/usr/bin/python
# -*- coding: utf-8 -*-



# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里
# 
# 老爸把字典翻了一遍
#   - 看到%s（单词）:%s(意思)

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）

# @author: B17455
def main():
  book = {"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"}

  index = 0
  num = len(book) 
  lst = [None]*num

  for key in book.keys():
    lst[index] = book[key]
    index = index + 1

  #print lst
  #str_1  = book['abase']
  print '老妈，在看一本英文书'

  if not book.has_key('etiquette'): #没有查到
    print '老妈没有查到%s的意思' % ('etiquette')

    #撕毁了abandon
    del book['abase']
    print '老妈撕毁了%s的页面' % ('abase')

    if book.has_key('abase'):
      print '老妈查到了%s:%s' % ('abase', book['abase'])

    else:
      #老爸黏贴了代码
      print '老妈没有查到%s' % ('abase')
      print '老妈把%s的字典页又贴上了' % ('abase') 
      book['abase'] = lst[2]
      print '老妈查到了%s:%s' % ('abase', book['abase'])
  else:
    print '老妈查到了%s'% ('etiquette')
    if book.has_key('abase'):
      print '老妈查到%s：%s'% ('abase',book['abase'])
      if book.has_key('abash'):
        print '老妈查到%s: %s'%('abash', book['abash'])

if __name__ == '__main__':
  main()