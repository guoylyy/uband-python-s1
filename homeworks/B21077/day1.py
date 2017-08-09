#-*-coding:utf-8 -*-
#@author:wendy
def main():
	who='wendy的老妈'
	good_price=1#小贩的价格
	good_description="西双版纳大白菜"#小贩的招牌
	is_cheap=False #是否便宜
	reasonable_price=5#老妈能接受的最高价格
	buy_amount=2#准备买2斤

	print "%s上街看到了%s，卖%d元/斤"%(who,good_description,good_price)

	if good_price<=reasonable_price:
		print'她认为便宜'
		is_cheap=True

		buy_amount=2+(reasonable_price-good_price)
		if buy_amount>4:
			buy_amount=4
		print"她买了%d斤"%(buy_amount)
			
	else:
		print'她认为贵了'
		is_cheap=False
		print'她并没有买，扬长而去'
if __name__ == '__main__':
	main()