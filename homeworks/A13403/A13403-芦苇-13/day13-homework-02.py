#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: luwei

def main():
	lst = ['pen','apple','pineapple']
	for lst_item in lst:
		print '老妈看到了 %s' %(lst_item)

try:
  lst = lst -1
except Exception,e:
  print e



if __name__ == '__main__':
  main()