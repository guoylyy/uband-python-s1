# -*- coding: utf-8 -*-

def main():

  pie_number = 6
  pie_price = 6.7159
  pie_total_price = pie_number * pie_price

  print pie_total_price
  
  #try to explain what's float
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %g ' % (pie_total_price)
  print 'pie cost %0.2f ' % (pie_total_price) #四捨五入
  print 'pie cost %0.3f ' % (pie_total_price)
  print 'pie cost %0.6f ' % (pie_total_price)

  #04. **
  number = 2**3
  print 'number = %d' % (number)

  #05. what else? 

  print 'test: %d' % (1 != 2)
  print 'test: %d' % (1 >= 2)

  if(2 == 2):
    print 'wweewe we w'
  else: 
    print 231

if __name__ == '__main__':
  main()