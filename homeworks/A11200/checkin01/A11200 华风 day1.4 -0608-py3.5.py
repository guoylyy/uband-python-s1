# -*- coding:utf-8 -*-
# @author:huafeng


#郭笃师的方法 扩展作业
def main():
  
  good_price = 2      #小贩的菜价格，每降低一元多买一斤
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2       #每降低一元多买一斤
  
  who = '华风的老妈'          
  good_description = '西双版纳大白菜'   #菜的品牌
  
  is_cheap = False  #是否便宜
 
  print ('%s上街看到了%s,卖%d元/斤'%(who,good_description,good_price))

  if good_price <= reasonable_price:   # 当菜价4元小于等于5元
    print ('她认为便宜')
    is_cheap = True
  #解决老妈买几斤的问题
  #5元-2斤 4-3 3-4 2-4
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4 :
      buy_amount = 4

    print ('她买了%d斤'%(buy_amount)) 

  else:
    print ('她认为太贵，没买，回了')


 # run function
if __name__ == '__main__':
   main()

  
