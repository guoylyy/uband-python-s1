# -*- coding: UTF-8 -*-

def main():
  tup = (1,2,3,4)
  print tup[1]
  print tup
  print tup[0:3]
  print tup[2:]
  print (1 in tup)
  print (5 in tup)

  a,b,c,d, = (1,2,3,4)
  print a
  print b
  print c
  print d
  print '---'
  for item in tup:
	print item
	
  print ' enumerate---'
  for index, item in enumerate(tup):
		print index

  try:
	tup.append(9)
	del tup[0]
	tup[0] = 'aaa'
  except Exception, e:
	 print e
		
if __name__ == '__main__':
  main()
	

	
	
