#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

#思考题
#What is float?
    #In computing, floats can be represented as: significand × base(2/10/16)*exponent.
    # %g 浮点数字(根据值的大小采用 %e浮点数(科学计数法)或 %f浮点数(小数点)
   #print 'pie cost %0.2f' % (pie_total_price) #f浮点数字(小数点后两位)
   
def main():
  pie_number = 6
  pie_price = 6.7
  x = 2
  y = 5  
  c = True
  d = False

  pie_total_price = pie_number * pie_price
  
  #float
  print 'pie cost %d' % (pie_total_price) #%d有符号整数(十进制)
  print 'pie cost %g' % (pie_total_price)  #%g 浮点数字
  print 'pie cost %0.2f' % (pie_total_price) #f浮点数字(小数点后两位)


 # 测试符号 
  print 'number = %d, %d, %d, %d' % (x + y, x - y, x * y, x ** y)
  print 'outcome = %d, %d, %d' % (x / y, y // x, y % x)
  print x & y   #二进制“与”运算: 两位同时为1才为1，否则为0。 特:清零：取指定位
  print x | y   #二进制“或”运算：两位只要有一个为1则为1。 特:对1
  print 'test: %d, %d, %d' % ( x != y,  x >= y, x == y)
  print 'test: %d, %d, %d' % ( not d, c and d, c or d)


if __name__ == '__main__':
  main()