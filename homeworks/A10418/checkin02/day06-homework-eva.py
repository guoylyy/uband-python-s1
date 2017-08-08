#!/usr/bin/python
# -*- coding: utf-8 -*-

def main1():


	lst=['cabbage','turnips','tomato','turtle','lobster','ginger','peony','pomelo','beef','dumpling']
	
	print 'mom went to the market'

	for index,lst_item in enumerate(lst):

		
		
		num=int(index)
		index2 = index+1

		if (num%2) == 0:
			
			print 'mom saw %s and bought %d kilogram. And she kept hanging around' %(lst_item,index2)

		else:
			print 'mom saw %s and did not buy it'%(lst_item)

			if (num+1)==10:
				print 'mom looked at things she had bought in hand, felt satisfied and went home'
			else:
				print 'mom kept hanging out'

	return index2

def main2():
	lst=['cabbage','turnips','tomato','turtle','lobster','ginger','peony','pomelo','beef','dumpling']
	
	lst.append('carrot')
	lst.append('potato')
	lst.append('pork')

	print 'mom went to the market'

	for index,lst_item in enumerate(lst):

		
		
		num=int(index)
		index2 = index+1

		if (num%2) == 0:
			
			print 'mom saw %s and bought %d kilogram' %(lst_item,index2)
			if (num+1)==13:
				print 'mom looked at things she had bought in hand, felt satisfied and went home'
			else:
				print 'And she kept hanging around'

		else:
			print 'mom saw %s and did not buy it'%(lst_item)

			print 'mom kept hanging out'

def main4(lst2):

	for lst2_item in lst2:
		print 'but she only bought %s'%(lst2_item)


def main3():
	lst=['cabbage','turnips','tomato','turtle','lobster','ginger','peony','pomelo','beef','dumpling']
	
	

	for lst_item in lst:
		print 'mom went to the market and saw %s'%(lst_item)

	lst2=lst[4:9]
	main4(lst2)


def main5():
	lst=['cabbage','turnips','tomato','turtle','lobster','ginger','peony','pomelo','beef','dumpling']
	

	for lst_item in lst:
		print 'mom went to the market and saw %s'%(lst_item)

	lst2=lst[4:9]

	return lst2



def main6(lst3):
	

	for lst3_item in lst3:
		print 'but she only bought %s'%(lst3_item)




if __name__ == '__main__':
	
	lst3=main5()
	main6(lst3)

	


