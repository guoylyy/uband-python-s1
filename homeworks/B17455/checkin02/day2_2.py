#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

def main():
  apple_num = 5
  apple_price = 4.8
  pie_num = 6
  pie_price = 6.7

  apple_total_price = apple_num * apple_price
  pie_total_price =pie_num * pie_price

  print 'pie cost %d '% (pie_total_price)
  print 'pie cost %g '% (pie_total_price)
  print 'pie cost %0.3f '% (pie_total_price)

  num=0.2**3
  print 'number = %0.5f' % (num)

  test = (num!=0)
  print test
  print 'the result of test is %d' % (test)



if __name__ == '__main__':
  main()