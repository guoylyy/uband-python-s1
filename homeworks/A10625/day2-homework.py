 #!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# Day2 - 为了大家能够做好这一次的第一个作业
#        继续深化变量的练习
#        
# homework2

def main():
  #01.int 
  apple_number = 5
  apple_price = 4.8
  pie_number = 6
  pie_price = 6.7

  


  #02. *  /
  apple_total_price = apple_number * apple_price
  print "apple_total_price = %d" % (apple_total_price)
  pie_total_price = pie_number * pie_price
  
  
  #03. try to explain what's float
  print 'pie cost %d ' % (pie_total_price)
  print 'pie cost %g ' % (pie_total_price)
  print 'pie cost %0.2f ' % (pie_total_price)#0是数字的宽度如果实际宽度小于指定宽度就无视指定宽度，如果小于指定宽度则前面用空格补全，2是小数位的个数

  #04. **
  number = 2**3#幂运算
  print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在限免测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
  print 'test: %d' % (1 != 2)
  print 'test: %d' % (1 >= 2)
  if 1:
    print 'goog'

  if 0:
    print 'xxx'####这两个例子都不会输出，因为if 需要条件为true才可以运行下面，这两个例子后面0 和（2 ！= 2）都是false

  if(2 != 2):
    print 'wweewe we w'
  #请开始你的表演

  #int
  print "开始试验"
  print apple_price
  print int(apple_price)#强行转化为整数类型，可以酱紫么。。。
  print float(apple_number)
  print "apple_total_price = %d" % (apple_total_price)

  per_price = pie_price / pie_number
  per_price = pie_price // pie_number
  test_1 = 7 % 2 #取得除法的余数
  print "%d" % (test_1)
  test_2 = 7 & 2 
  print "%d" % (test_2)
  test_3 = 1 & 2 
  print "%d" % (test_3) 
  #按位与运算符：参与运算的两个值,如果两个相应位*都为1*,则该位的结果为1,否则为0（7的二进制 0111， 2二进制0010 输出结果0010 是2； 1二进制01 2二进制10 输出00 所以是0  ）
  test_4 = 1 | 2
  print "%d" % (test_4)##按位或运算符：参与运算的两个值,如果两个相应位*有一个为1*,则该位的结果为1,否则为0（7的二进制 0111， 2二进制0010 输出结果0111 是7； 1二进制01 2二进制10 输出11 所以是3  ）

  test_5 = 5 ^ 2 #按位异或，相同为假，不同为
  

if __name__ == '__main__':
  main()