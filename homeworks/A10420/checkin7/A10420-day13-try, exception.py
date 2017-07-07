# -*- coding: utf-8 -*-

def main():
  week_overnight = [True, False, True, False, True] 
  for index, is_overnight in enumerate(week_overnight):
    print '今天星期 %d' % (index + 1)
    
    try:
      overnight_check(is_overnight)
    except Exception, e:
      print '发生错误：%s' % (e)
      print '老妈骂了老爸一顿，然后原谅了他'
    else:
      print '什么都没发生'

def overnight_check(is_overnight):   
  if is_overnight:
    raise Exception('老爸夜不归宿')
  else: 
    print '正常'

if __name__ == '__main__':
   main()

# 在day1～day12的代码中任意找一个你以前犯过的错，try一发，输出一个错误看下是不是会继续走下去，截图打卡。