# -*- coding:utf-8 -*-

def record_account(is_cheap4,total_pay3):
  if is_cheap4:
    print '老妈在小本子记了买菜花销 %d 元' % (total_pay3)

def talk_with_dad(is_cheap3,buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说: "今天去买菜，价格不贵，买了 %d 斤".' % (buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买".'

def buying():
  good_price = 4 #小贩的价格
  buy_amount = 2 #准备买 2 斤
  reasonable_price = 5 #老妈能接受的最高价格
  
  who = "一九零的老妈"
  good_description = "西双版纳大白菜" #小贩的招牌
  
  is_cheap = False #是否便宜
  

  print '%s上街看到了%s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:
      print '她认为便宜'
      is_cheap = True
      buy_amount = 2 + (reasonable_price - good_price)
      if buy_amount > 4:
        buy_amount = 4
      total_pay = buy_amount * good_price
      print '她买 %d 斤' % (buy_amount)
  else:
      print "她认为贵了"
      is_cheap = False
      print "她并没有买，扬长而去"

  return is_cheap,buy_amount,total_pay

  def main():
    is_cheap2, buy_amount2, total_pay2 = buying()
    talk_with_dad(is_cheap2, buy_amount2)
    record_account(is_cheap2, total_pay2)

  if __name__ == '__main__':
    main()
