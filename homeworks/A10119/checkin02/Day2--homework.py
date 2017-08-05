#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan

#homework 2
def main():
  print 'test1: %d' % (1 > 2)
  print '%d' % (2 + 3)
  print '%d' % (7 - 4)
  print '%d' % (8 * 9)
  print '%d' % (3 ** 4)
  print '%g' % (15.0 / 4)
  print '%g' % (15 // 4)
  print '%d' % (8 % 3)
  if (3 < 5):
  	print 'YES'
  if(3 <= 6):
  	print 'right'
  print 'test2: %d' % (3 >= 6)
  print 'test2: %d' % (2 == 2)
  if(2 != 3):
    print 'It is not the same'
  if(2 > 3 and 4 < 5):
  	print 'It is good'
  else:
  	print 'It is bad'
  if(2 > 3 or 4 < 5):
  	print 'It is reluctant'
if __name__ == '__main__':
  main()