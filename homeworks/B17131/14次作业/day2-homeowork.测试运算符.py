#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

def main():
  #1. 加法
  number=	2+3
  print 'number=%d' % (number)
  
  #2. 减法
  number=	2-3
  print 'number=%d' % (number)

  #3. 乘法
  number=  2*3
  print 'number=%d' % (number)
	
  #4.幂
  number= 2**3
  print 'number=%d' % (number)

  #5.除
  number= 4/3.0
  print 'number=%g' % (number)

  #6.取整除
  number= 4//3.0
  print 'number=%d' % (number)
	
  #7.小于
  print 'test: %d' % (5<4)
	
  #8.大于
  print 'test: %d' % (5>3)
	
  #9.小于等于
  print 'test: %d' % (5<=3)
	
  #10.大于等于
  print 'test: %d' % (9>=6)
	
  #11.等于等于
  print 'test: %d' % (10==10)
	
  #12.不等于
  print 'test: %d' % (2!=2)
	

if __name__ == '__main__':
  main()
  