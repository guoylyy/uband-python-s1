#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

 
def main():
  #01.int 
  apple_number = 5
  pear_number = 6
  apple_price = 4.8
  new_price = 7
  original_price = 6
  pie_number = 6
  pie_price = 6.7
  goal = 500
   
  #02. *  /
  fruit_number = apple_number + pear_number
  margin = new_price - original_price
  apple_total_price = apple_number * apple_price
  pie_total_price = pie_number * pie_price
  set_number = goal / margin 
  #03. 
  print 'apple_total_price % g' % (apple_total_price)
  print 'margin %d ' % (margin)
  print 'pie cost %0.2f ' % (pie_total_price)
 
  #04. **
  number = 2**3
  print 'number = %d' % (number)
 
  #05.
  print 'test: %d' % (1 != 2)
  print 'test: %d' % (1 >= 2)
  if 1:
    print 'right'
  if 0:
    print 'wrong'
 
  if(2 != 2):
    print 'yes'
 
if __name__ == '__main__':
  main()