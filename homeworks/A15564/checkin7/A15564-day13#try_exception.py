#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
  week_overnight = [True, False, True, False, True] # Monday through Friday
  for index, is_overnight in enumerate(week_overnight):
    print '今天星期 %d' % (index + 1)
    
    try:
      overnight_check(is_overnight)
    except Exception, e:
      # if error occurs
      print '发生错误：%s' % (e)
      print '老妈骂了老爸一顿，然后原谅了他'
    else:
      # no error
      print '什么都没发生'

def overnight_check(is_overnight): 
  # checking mechanism
  if is_overnight: # Dad's out overnight
    raise Exception('老爸夜不归宿')
  else: # Dad comes home
    print '正常'

# if __name__ == '__main__':
#   main()

# try_except example
#1
def error_material1():
  week_overnight = [True, False, True, False, True] # Monday through Friday
  index = 0
  for index, is_overnight in week_overnight:
    print is_overnight

def try_except1():
  try:
    error_material1()
  except Exception, e:
    print e

#2
def error_material2():  #too many values to unpack
  week_overnight = ['True', 'False', 'True', 'False', 'True'] # Monday through Friday
  index = 0
  for index, is_overnight in week_overnight:
    print '今天星期 %d' % (index + 1)
    index = index + 1
    print is_overnight

def try_except2():
  try:
    error_material2()
  except Exception, e:
    print e

if __name__ == '__main__':
  print '#1'
  try_except1()
  print '#2'
  try_except2()