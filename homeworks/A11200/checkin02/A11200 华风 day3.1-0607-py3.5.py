# -*- coding: utf-8 -*-
# @author: Huafeng

# 1. function(code block)
#    one file multiple function(code block)
# 2. return (pass variable)    #传递变量
# 3. return mutiple variables   #多个变量
# 
# #原则# 单一职责原则理解 : 一段代码 只执行一个功能，便于模块化，也便于堆砌更多功能组合成大功能。
#  一段代码不要附加太多功能，避免别的地方调用其他功能，却要做修改时，这时会影响原来的第一个功能。
# 从而造成包含第一个功能的那部分功能发生紊乱。
#  也有不好的地方，要对各段代码之间的逻辑关系非常清楚，有时可以近似的功能调用却要多写一段代码。
# 
def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print ('老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3))
  else:
    print ('老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。')

def buybuybuy():
  good_price = 4 #每降低一元，多买一斤
  reasonable_price = 5
  buy_amount = 2 #每降低一元，多买一斤
  
  who = 'xiao的老妈'
  good_description = '西双版纳大白菜'

  is_cheap = False

  print ('%s上街看到了%s，卖 %d 元/斤' % (who, good_description, good_price))

  if good_price <= reasonable_price:
    print ('她认为便宜')
    is_cheap = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print ('她买了 %d 斤' % (buy_amount))
  else:
    print ('她认为贵了 ')
    is_cheap = False
    print ('她并没有买，扬长而去')

  return is_cheap, buy_amount

def main():

  is_cheap2, buy_amount2 = buybuybuy()

  talk_with_daddy(is_cheap2, buy_amount2)  
  

if __name__ == '__main__':
  main()
