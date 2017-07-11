#!/usr/bin/python
#	-*coding:	utf-8	-*-
#	@author:yuanyi
def main():
	book	=	{
					"abandon":'to give up to the control or influence of another person or agent',
					"abase":'to lower in rank,office,prestige,or esteem',
					"abash":'to destory the self-possession or self-confidence of'
					}
	print	'老妈先查了一个单词%s没有查到'	%('etiquette')
	if not	book.has_key('etiquette'):
		print	'老妈没有查到%s的意思'	%('etiquette')
		del	book['abase']
		print	'老妈把含有%s一页的单词撕掉了'	%('abase')
	else:
		print	'老妈查到了 %s'	%(etiquette)

	print	'老妈又查了一个单词%s得到了解释'	%('abase')		
	if book.has_key	('abase'):
		book['abandon']	=	'to give up to the control or influence of another person or agent'
		print	'老妈很开心，又把%s加入到了字典里'	%('abandon')
	else:
		print	'老妈没有查到%s'	%('abase')

	print	'老妈把单词翻了一遍'
	for key in book.keys():
		print	'老妈看到了%s:'	%(key)
		print	book[key]
		
if __name__ == '__main__':
	main()