#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
	overnights=[False,False,True,False,False]
	for index, item in enumerate(overnights) :
		try:
			print "今天是周%d"%(index+1)
			over_night(item)
		except Exception,e:
			print e
			print "老妈骂了老爸后，原谅了他"
		else:
			print "脚本文件"

def over_night(overnight):
	if overnight==True:
		raise Exception("离婚")
	else:
		print "按时回家"


if __name__ == '__main__':
	main()