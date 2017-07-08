def overnight_check(item):
  if item:
   raise Exception('divorce')
  else: 
   print 'good'

def main():
 print 'yes'
 week_overnight = [False, False, True, False, False]

 for index, item in enumerate(week_overnight):
  print 'today is %d' % (index + 1)
  try:
   overnight_check(item)
  except Exception,e:
   print 'error: %s' % (e)
   print 'shit happens'
  else:
   print 'all is well'


 
if __name__ == '__main__':
  main()