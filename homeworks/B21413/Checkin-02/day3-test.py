# -*- coding:  utf-8 -*-

def main():
	pear_numeber = 6
	pear_price = 6.8
	peach_number = 4
	peach_price = 15

	pear_total_price = pear_price - pear_numeber
	peach_total_price = peach_price // peach_number

	print 'peach cost %d' % (peach_total_price)
	print 'peach cost %s' % (peach_total_price)
	print 'peach cost %0.2f'% (peach_total_price)

if __name__ == '__main__':
	main()