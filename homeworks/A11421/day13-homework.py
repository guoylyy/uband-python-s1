#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  late = [False, False, True, False, False]
  for index, status in enumerate(late):
    try:
      relation (status, index)
    except Exception, e:
      print e

def relation(status, index):
  if not status:
    print "星期%d，正常" % (index+1)
  else:
    raise Exception("星期%d，大吵一架"% (index+1))
  
if __name__ == '__main__':
  main()


