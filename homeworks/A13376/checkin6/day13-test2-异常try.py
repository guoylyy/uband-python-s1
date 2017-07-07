#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yikuai


def main():

  tuple = ( 1,2,3,4 )
  print tuple

  print '-----try------'

  try:
  	del tuple[0]
  except Exception,e:
  	print 'you are wrong' 
  else:
  	print 'emmm'

  print '-----I am ok---I can still work-----'

# run function
if __name__ == '__main__':
  main()