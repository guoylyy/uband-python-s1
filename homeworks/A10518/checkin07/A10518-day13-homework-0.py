#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:fanyujie

def main():
  stay_out = [False, False, True, False, False]
  for index,status in enumerate(stay_out):
    print 'This is day%d' % (index + 1)

    try:
      check(status)
    except Exception,e：
      print 'Shit happens:error %s' % (e)
    else:
      print 'Never be better'


def check(status):
  if status:
    raise Exception('warning')
  else:
    print 'All is well'


if __name__ == '__main__':
  main()
