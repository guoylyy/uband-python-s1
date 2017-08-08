#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小仙女

def main():
	print"老爸在看一本英文书，字典只有三个词的解释，分别是"
	dictionary={
							"abandon": "to give up to the control or influence of another person or agent",
							"abase":  "to lower in rank, office, prestige, or esteem ",
							"abash":  "to destroy the self-possession or self-confidence of "
							}
  	for key in dictionary.keys():
  		print key
  		print dictionary[key]
	print"老爸先查了一个单词'etiquette'"
	if dictionary.has_key('etiquette'):
		print "查到了"
	else:
		print"没有查出来"
		print"老爸怒了，把含有'abandon'一页的单词撕掉了"
	del dictionary["abandon"]
	print"此时只剩下"
	for key in dictionary.keys():
		print key
	print"老爸又查了一个单词'abase'"
	if dictionary.has_key("abase"):
		print"得到了解释，老爸很开心，又把'abandon'加入到字典里"
		dictionary["abandon"]="to give up to the control or influence of another person or agent"
		print"此时字典有"
		for key in dictionary.keys():
  			print key
  			print dictionary[key]
	else:
		print"没查到"
  




if __name__ == '__main__':
  main()							