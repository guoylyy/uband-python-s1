#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	book = {
	"abandon": 'to give up to the control or influence of another person or agent',
	"abase": "to lower in rank, office, prestige, or esteem",
	"abash" : "to destroy the self-possession or self-confidence of"
	}
	who = '老妈'
	tear_word = 'abase'
	tear_mean = book[tear_word]
	#我觉得前面将函数定义好之后，便于之后的取值，很方便，节省码字；
	#其实，这样真的很便捷，看了这里的代码和前一个作业的代码，感觉这个清爽又简洁，看着也舒服。
	#我根本想不到用一个新的函数来定义，今后仍需不断努力，其实代码的逻辑清晰，结构简洁
	print '%s 在看一本英文书' % (who)
	if not search('etiquette', book, who):#为什么有三个量
		
		del book[tear_word]
		print '%s 撕毁了 %s 的页面' % (who,tear_word)

		book[tear_word] = tear_mean 
	#我觉得这部分应该写在if语句外面，否则就没有添加进去，因为if判断出来没有abase这个单词
		if search('abase', book, who):			
			print '%s 把%s 的字典页面又贴上了' % (who, tear_word)
	print '------'
	if search('abash',book,who):
		pass 
	#本来不知道这里该写什么的，因为函数定义中，已经print出需要的语句，所以就不需要print语句的输入。我想不写点东西，这个就会报错，所以写了pass
	if search('abase',book,who):
		pass
	print '----'
#定义函数search 起先一直看不懂这块在干吗（我以为search函数这个是默认的，但是百度了下没有= =#），后来试了下把这部分去掉，结果就出现该函数没有定义，这才看懂了函数
def search(key,dictionary,who):
	if dictionary.has_key(key):
		print '%s 查询到了了%s: %s' % (who, key, dictionary[key])
		return True
	else:
		print '%s 没有查询到 %s 的意思' % (who,key)
		return False

if __name__ == '__main__':
	main()