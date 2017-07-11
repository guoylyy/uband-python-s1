#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

#1.把老爸换成老妈，做的时候数一数改了几处代码
#答：七处代码
#2.把撕毁的页码换成'abase'，做的时候数一数改了几处代码
#答：七处代码
#3.想想如何让最后粘贴回撕毁代码页的时候不用重复再打一遍释义
#4.如果查到就打印：'老爸查到了%s：%s'，写代码让老爸再搜索'abase''abash'这两个单词，数一数有多少出重复的打印代码

def homework2():
	book = {"abandon":'to give up to the control or influence of another person or agent',
			"abase":'to lower in rank, office,prestige, or esteem',
			"abash":'to destroy the self-possession or self-confidence of'
			}
	who = '老爸'
	tear_word ='abandon'
	print '%s在看一本英文书'%(who)
	if not search('etiquette',book,who): #没有查到
		tear_mean = book[tear_word]
		
		#撕毁了['abandon']
		#作业题2要求替换
		del book[tear_word]
		print '%s撕毁了%s的页面' %(who, tear_word)


		if search ('abase',book,who):
			#print '老妈查到了 %s：%s' %('abash', book['abash'])
			
			#老爸又把撕掉的贴回去了
			book[tear_word]=tear_mean
			print '%s把%s的字典又添加上去了'%(who,tear_word)
		#else:
			#print '老妈没有查到 %s' %(abash)
	#else:
		#print '老妈查到了 %s' %('etiquette')

def  search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s 查询到了%s：%s' %(who,key,dictionary[key])
		return True
	else:
		print '%s 没有查询到%s的意思' %(who,key)
		return False

if __name__ == '__main__':
	homework2()