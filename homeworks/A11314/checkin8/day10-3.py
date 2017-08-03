#!/usr/bin/python
# -*- coding:utf-8 -*-


def homework2():
	book = {
	  "abandon": 'to give up to the control or influence of another person or agent',
	  "abase": "to lower in rank, office, prestige, or esteem",
	  "abash" : "to destroy the self-possession or self-confidence of"
	  }
	who = "老爸"
	key1 = 'abase'
	value1 = 'to lower in rank, office, prestige, or esteem'
	
	print "%s正在看一本因为书" %(who)
	if not search(book,who,'etiquette'):
		del book[key1]
		print "%s撕毁了 %s 的页面" %(who,key1)
		if search(book,who,'abandon'):
			book[key1]=value1
			print "%s把 %s 的字典页又贴上了" %(who,key1)

	search(book,who,list())

def search(book,who,key):
	if book.has_key(key):
		print "%s找到了%s的信息" %(who,key)
		return True
	else:
		print "%s没有查到%s的信息" %(who,key)
		return False

def list():
	lst = ["abase","abash"]
	for lst_item in lst:
		print lst_item


if __name__ == '__main__':
	homework2()