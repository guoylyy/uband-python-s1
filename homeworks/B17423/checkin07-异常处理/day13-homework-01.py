#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

def main():
	week_overnight = [False, False, True, False, False]

	for index, is_overnight in enumerate(week_overnight):
		print ("今天星期 %d" % (index +1))

		try:
			overnight_check(is_overnight)
		except Exception as e:
			print ("发生错误：%s" % e)
			print ("老妈骂了老爸一顿，然后原谅了他")
		else:
			pass
		finally:
			pass


def overnight_check(is_overnight):
	if is_overnight:
		print ("老爸夜不归宿")
		raise Exception('离婚')
	else:
		print ("正常")


if __name__ == '__main__':
	main()