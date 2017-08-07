#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

#sublime输出不全qaq 试过是对的
def homework2():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老爸'
	tear_word = 'abandon' #可能会被撕毁的页的key

	print '%s在看一本英文书' % (who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print '%s撕毁了 %s 的页面' % (who, tear_word)

	if search('abase', book, who):
      #老爸黏贴了代码
		book[tear_word] = tear_mean
		print '%s把 %s 的字典页又贴上了' % (who, tear_word)


def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
		return True
	else:
		print '%s 没有查询到 %s 的意思' %(who, key)
		return False

#1 改了一处
def homework21():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老妈'
	tear_word = 'abandon' #可能会被撕毁的页的key

	print '%s在看一本英文书' % (who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print '%s撕毁了 %s 的页面' % (who, tear_word)

	if search('abase', book, who):
      #老妈黏贴了代码
		book[tear_word] = tear_mean
		print '%s把 %s 的字典页又贴上了' % (who, tear_word)

#2 改了一处
def homework22():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老爸'
	tear_word = 'abase' #可能会被撕毁的页的key

	print '%s在看一本英文书' % (who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print '%s撕毁了 %s 的页面' % (who, tear_word)

	if search('abase', book, who):
      #老爸黏贴了代码
		book[tear_word] = tear_mean
		print '%s把 %s 的字典页又贴上了' % (who, tear_word)

#4 没有重复的打印代码
def homework24():
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
			"abase": "to lower in rank, office, prestige, or esteem",
			"abash" : "to destroy the self-possession or self-confidence of"
			}
	who = '老爸'
	tear_word = 'abandon' #可能会被撕毁的页的key

	print '%s在看一本英文书' % (who)
	if not search('etiquette', book, who):
		tear_mean = book[tear_word]

		del book[tear_word]
		print '%s撕毁了 %s 的页面' % (who, tear_word)

	if search('abase', book, who):
      #老爸黏贴了代码
		book[tear_word] = tear_mean
		print '%s把 %s 的字典页又贴上了' % (who, tear_word)

	search('abash', book, who)
	search('abandon', book, who)



if __name__ == '__main__':
	homework2()
	homework21()
	homework22()
	homework24()



#两段代码比较总结：
#让代码简洁的方法
#尽量不要直接使用某个参数（如这里的‘老爸’），而是使用变量赋值，然后调用变量。
#对于要重复执行的代码可以定义一个函数，调用函数。
