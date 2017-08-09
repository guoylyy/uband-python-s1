#-*-coding:utf-8 -*-
#@author:wendy
def talk_with_daddy(is_cheap3,buy_amount3):
	if is_cheap3:
		print'老妈对老爸说菜便宜买了,买了%d斤'%(buy_amount3)
	else:
		print'老妈对老爸说菜贵了没买'
def money_account(is_cheap4,buy_amount4):
	if is_cheap4:
		print'老妈记账在本子上，写下买了%d斤'%(buy_amount4)
	else:
		print'老妈没有记账因为没买东西'

def buybuybuy():
	who='wendy的老妈'
	good_price=5#小贩的价格
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
	return is_cheap,buy_amount
if __name__ == '__main__':
	is_cheap2,buy_amount2=buybuybuy()
	talk_with_daddy(is_cheap2,buy_amount2)
	money_account(is_cheap2,buy_amount2)