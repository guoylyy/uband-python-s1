
# -*-coding: utf-8 -*-
# @author: Shuan

def main():
  #01.int 
 apple_number = 5
 apple_price = 4.8
 pie_number = 6
 pie_price = 6.7

 #02. * /
 apple_total_price = apple_price*apple_number
 pie_total_price = pie_price*pie_number

 #03. 
 print 'pie cost %d' %(pie_total_price)
 print "pie cost %g"%(pie_total_price)
 print "pie cost %0.2f" %(pie_total_price)
 
 #04. **
number = 2**4
print'number=%d'%(number)

#05. /  //
a= 4/5.0
b= 4//3

print "c= %0.2f+%d"% (a,b)

#06. <= >= ==
def main():
 x=23; y=9 ;z=20
 if x>=y:
 	print y
 elif y==z:
 	print z
 else:
 	print x



if __name__ == '__main__':
  main()