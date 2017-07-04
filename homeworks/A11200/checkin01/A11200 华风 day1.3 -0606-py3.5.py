# -*- coding:utf-8 -*-
# @author:huafeng


#笨办法算
def main():
  who = '华风的老妈'
  good_price1 = 4   #小贩的菜价格1，先来笨办法，不用其他语句
  good_price2 = 3   #小贩的菜价格2，先来笨办法，不用其他语句
  good_price3 = 2   #小贩的菜价格3，先来笨办法，不用其他语句
  good_description = '西双版纳大白菜'   #菜的品牌
  
  is_cheap = False  #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount1 = 2 #准备买2斤，此时价格4元
  buy_amount2 = 3 #准备买3斤，此时价格4元
  buy_amount3 = 4 #准备买4斤，此时价格4元

  #试试
  print ("%s上街看到了%s,卖%d元/斤"%(who,good_description,good_price1))

  if good_price1 <= reasonable_price:   # 当菜价4元小于等于5元
    print ('她认为便宜')
    is_cheap = True
    print ("她买了%d斤"%(buy_amount1))  # 菜价4元 买2斤

    print ("%s上街看到了%s,卖%d元/斤"%(who,good_description,good_price2))

    if good_price2 <= reasonable_price: #当菜价3元小于等于5元
      print ('她认为便宜')
      is_cheap = True
      print ("她买了%d斤"%(buy_amount2))  # 菜价3元 买3斤

      print ("%s上街看到了%s,卖%d元/斤"%(who,good_description,good_price3))

      if good_price3 <= reasonable_price: #当菜价2元小于等于5元
        print ('她认为便宜')
        is_cheap = True
        print ("她买了%d斤"%(buy_amount3))  # 菜价2元 买4斤
      else:
        print ('她认为贵了')
        is_cheap = False
        print ('她没买，扬长而去')

    else:
  	  print ('她认为好贵，没买，走了')
    

  else:
    print ('她认为太贵，没买，回了')

  return "main"
 # run function
if __name__ == '__main__':
   main()

  
