#!/usr/bin/python
#filename:practice.py
def decision(index):
	if (index % 2==0):
		return True 
	else:
		return False
def main():
	buy_amount=0
	index=0

	lst = ['cabbage', 'rabbish', 'tomato', 'turtle', 'loster','ginger','white peony root','grapefruit','beef', 'dumpling']
	print 'mom came to the market'
	for lst_item in lst:
		if decision(index):
			buy_amount=index+1
			print 'my mon saw %s,and she bought %d jin'%(lst_item,buy_amount)
		else:
			print 'my mom saw%s'%(lst_item)
		index=index+1

		if index<10:
			print 'my mom continued to shop'
		else:
			print 'my mom went home'
if __name__ == '__main__':
	main()
	




