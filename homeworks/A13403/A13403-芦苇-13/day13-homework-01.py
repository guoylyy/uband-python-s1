#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
  week_overnight = [False, False, True, False, False] #周一到周五的情况
  for index,is_overnight in enumerate(week_overnight):
    print '今天星期%d' % (index + 1)
    
    try:
      overnight_check(is_overnight)
    except Exception,e:
      print '发生错误：%s' % (e)
      print '老妈骂了老爸一顿，然后原谅了他'
    else:
      print '附带脚本'

# func. 离婚处理程序
# 如果老爸夜不归宿
# 启动离婚程序
def overnight_check(is_overnight):
  if is_overnight:
    raise Exception('离婚') #强行中断程序的语法
  else:
    print '正常'

if __name__ == '__main__':
  main()