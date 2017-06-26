#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: bettyyan

def main():
  week_overnight = [False, False, True, False,False] #周一到周五的情况
  for index,is_overnight in enumerate(week_overnight):
    print '今天星期%d' %(index + 1)

    try:
      overnight_check(is_overnight)
    except Exception,e:
       #发生错误的情况
      print 'error: %s' % (e)
      print '老妈骂了老爸一顿，然后原谅了他'
    else:
       #没有发生错误的情况
      print 'everthing was ok'

# func. 离婚处理程序
# 如果老爸夜不归宿
# 启动离婚程序
def overnight_check(is_overnight):
  if is_overnight:
    raise Exception('devorce') #强行中断程序的语法
  else:
    print 'nothing happened'

  
if __name__ == '__main__':
  main()


