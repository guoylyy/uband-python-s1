#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
def main():
  
  a = 1.5
  b = 2
  c = 3.2
  d = 4

  xxx = (a + b) * (d - c) 

  print 'xxx %d ' % (xxx)
  print 'xxx %g ' % (xxx)
  print 'xxx %0.2f ' % (xxx)

  yy = d ** b

  print 'yy %d ' % (yy)

  print 'tt: %d ' % (2 != 2)

  if b >= a:
  	print 'lala'
  	
  

if __name__ == '__main__':
  	main()