#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小白

def main():

  overnight = [False, False,False, True, True]
  
  index = 0
  for is_overnight in overnight:
    index = index +1
    print '今天是星期%d' % (index)
 
    try:
      overnight_check(is_overnight)
    except Exception,e:
      print e


def overnight_check(is_overnight):
  if is_overnight:
    raise Exception('吵架')
  else:
    print '正常'
  
if __name__ == '__main__':
  main()
