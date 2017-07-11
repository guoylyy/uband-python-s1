#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin


def main():
  week_overnight = [False, False, True, False, False]

  for index, is_overnight in enumerate(week_overnight):
    print '今天星期 %d' % (index + 1)   #星期数的赋值 index是个重点
    overnight_check(is_overnight)    #使用下一个动作

def overnight_check(is_overnight):  #把is_overnight的值返进来
  if is_overnight:
    raise Exception('离婚')  #强行中断程序的语法
  else:
    print '正常'

print '------以上是直接报错的情况------'

def main2():
  week_overnight = [False, False, True, False, False]

  for index, is_overnight in enumerate(week_overnight):
    print '今天星期 %d' % (index + 1)   #星期数的赋值 index是个重点
    try:
      overnight_check(is_overnight)    
    except Exception, e:          #除了出现错误的时候，打印下面这段话
      print '发生错误，%s' % (e)    # e表示错误，在下面已经写了‘离婚’
      print '老妈骂了老爸一顿，然后原谅了他'
    else:
      print '附带脚本'   #没有发生错误的情况。用的并不多

def overnight_check(is_overnight):  #把is_overnight的值返进来
  if is_overnight:
    raise Exception('离婚')  #强行中断程序的语法
  else:
    print '正常'

#尝试用try在1~12天里掩饰
def try_error():
  lst = [1,2,3,4]

  print lst

  del lst

  try:
    print lst[0]
  except Exception as e:
    print 'there is an error'




if __name__ == '__main__':
  #main()
  main2()
  try_error()

