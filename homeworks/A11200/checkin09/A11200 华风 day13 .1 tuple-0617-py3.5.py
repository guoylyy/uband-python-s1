#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

# 注意 2.7版本和3.5版本的区别
# 2.7版本 except Exception,e 
# 3.5版本 except Exception as e

def main():
  week_overnight = [False, False, True, False, False]

  for index, is_overnight in enumerate(week_overnight):
    print ('今天星期 %s '% (index + 1))
    try:
      over_nightcheck(is_overnight)
    except Exception as e :
      print ('发生错误 %s'%(e))
    else :
      print ('附带脚本')

# 老爸夜不归宿，就启动离婚程序
def over_nightcheck(is_overnight): 
  if is_overnight :
    raise Exception('离婚')
  else :
    print ('正常')

if __name__ == '__main__':
  main()


