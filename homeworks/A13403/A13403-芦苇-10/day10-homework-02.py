#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: luwei

# 实现了和 homework01 一样的功能
# 供你分析和对比
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

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码
# 答：1处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
# 答：1处
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 答：(不太明白题目的意思)

def homework2():
	book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }

	who = '老爸'
	tear_word = 'abandon' #可能会被撕毁的页的key

	print ' %s 在看一本英文书' %(who)
	if not search ('etiquette',book,who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print ' %s 撕掉了 %s 的页面' % (who,tear_word)

		if search('abase',book,who):
			book[tear_word] = tear_mean
		print ' %s 把 %s 的字典页又贴上了' %(who, tear_word)

def search(key,dictionary,who):
	key = 'abase'
	if dictionary.has_key(key):
		print ' %s 查询到了 %s ：%s' %(who,key,dictionary[key])
		return True
	else:
		print ' %s 没有查询到 %s 的意思' %(who,key)
		return False


if __name__ == '__main__':
  homework2()