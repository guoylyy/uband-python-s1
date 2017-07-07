#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

#tab 键 今天把蜀黍的代码复制过来，发现不能运行，结果是因为空格的缘故，重新敲Tab

def homework2():
	who = ' 老妈 ' #将老爸替换成老妈 7处
	book = {
	"abandon": 'to give up to the control or influence of another person or agent',
	"abase": "to lower in rank, office, prestige, or esteem",   
	"abash" : "to destroy the self-possession or self-confidence of"
	}
	print '%s 在看一本英文书' % (who)
	if not book.has_key('etiquette'): 
		print '%s 没有查到 %s 的意思' % (who,'etiquette')
		#撕毁了abandon
		del book['abase']#将abandon替换abase 2处
		print '%s 撕毁了 %s 的页面' % (who,'abase') 
		book['abase'] = 'to lower in rank, office, prestige, or esteem'
		print '%s 把 %s 的字典页又贴上了' % (who,'abase')
		
		if book.has_key('abase'):
			print '%s 查到了 %s : %s' % (who,'abase', book['abase'])
		else:
			print '%s 没有查到 %s ' % (who,'abase') 
		if book.has_key('abash'):
			print '%s 查到了 %s : %s' % (who,'abash', book['abash'])	
		#老爸黏贴了代码
		else:
			print '%s 没有查到 %s ' % (who,'abash') 
	else:
		print '%s 查到了 %s '% (who,'etiquette')

if __name__ == '__main__':
  homework2()