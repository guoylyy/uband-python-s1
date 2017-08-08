#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小仙女

def main():
	dictionary={
							"abandon": "to give up to the control or influence of another person or agent",
							"abase":  "to lower in rank, office, prestige, or esteem ",
							"abash":  "to destroy the self-possession or self-confidence of "
							}
	print len(dictionary)
	print dictionary.keys()
	print dictionary.values()
	print dictionary.has_key("abandon")
	print dictionary.has_key("sad")
	dictionary["sad"]="unhappy or showing unhappiness"
	print len(dictionary)
	del dictionary["sad"]
	print len(dictionary)
	print dictionary["abandon"]
	if dictionary.has_key("sad"):
		print dictionary["sad"]
	else:
		print"一点都不sad"

	for key in dictionary.keys():
		print key
		print dictionary[key]
if __name__ == '__main__':
  main()		