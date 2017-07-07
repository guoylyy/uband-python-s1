def main():
  who = 'Mom'
  good_price = 4  
  good_description = "veg"
  is_cheap = False 
  reasonable_price = 5 
  buy_amount = 2 


  print "%s sees %s sold at %d dollars per gram" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print 'She thinks the price is reasonable'
    is_cheap = True
    print 'so she buys %d grams' % (buy_amount)
  else:
    print 'She thinks it is too expensicve to buy'
    is_cheap = False
    print 'so she leaves'

# run function
if __name__ == '__main__':
  main()

