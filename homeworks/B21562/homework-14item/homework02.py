#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

def main():
  #01.int 
  total_apple_price = 100
  apple_number = 30.0 #这里如果只输入整数的话，除法计算出的结果也只以整数来显示
  pie_number = 53
  pie_price = 2.98
  
  #02. *  /
  apple_price = total_apple_price / apple_number
  pie_total_price = pie_number * pie_price
  
  #03. try to explain what's float
  print '每个苹果价值 %d 元' %(apple_price) #d表示计算结果取整数
  print '每个苹果价值 %g 元' %(apple_price) #g表示计算结果取小数，默认显示6位有效数字，无意义的0不显示
  print '每个苹果价值 %f 元' %(apple_price) #f表示计算结果取小数，默认显示小数点后6位，无意义的0同样显示
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %0.2g ' % (pie_total_price) #写在g前面的0.2，表示计算结果只显示2位有效数字，采用科学计数法来显示结果
  print 'pie cost %0.2f ' % (pie_total_price) #写在f前面的0.2，表示计算结果显示小数点后2位

  #04. **
  number = 2**0.5 #一个乘号表示相乘关系，两个乘号表示幂
  print number
  print 'number = %0.3g' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2)
  if 1:
    print 'good'
  print 'test: %d' % (1 >= 2)
  if 0:
    print 'bad'
  if 1:
    print "why"
  print (1>=2)
  if(2 != 2):
    print 'wweewe we w'
  else:
    print "ok"
  #请开始你的表演
  print "a+b= %s" %('a'+'b')
  print "3.6+1.7=%d" %(3.6+1.7)
  print "3.6+1.7=%g" %(3.6+1.7)
  print "3.6+1.7=%0.2f" %(3.6+1.7)
  print -5.3
  print 2**(1/2.0)
  print 'la'*3
  print 4/3
  print 4.0/3
  print 4//3.0
  print 5%2
  print 5<3
  print "%d"%(5<3)
  x=3
  y=3
  print "%d"%(x==y)
  z=5
  print "x==z?%d"%(x==z)
  print x!=z
  print x>=z
  print x<z
  x=True
  y=False
  z=1
  print (x and y)
  print (x and z)
  print (x or y)
  print (y or z)
  print 1+5*6**2-3.0/3*(8-2)
  print 1+5*(6**2)-3.0/3*(8-2)
  print 1+(5*6)**2-3.0/3*(8-2)
if __name__ == '__main__':
  main()