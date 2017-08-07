#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    tup.append(9)#-------SyntaxError: invalid syntax
    print '---我就想知道这句话会不会执行---'#-----不会被执行。
    
  except Exception,e:
    print '元祖不能进行增加操作'
  else:
    print '今天周六'
  finally:
    print '下午可以看女排比赛'

if __name__ == '__main__':
  main()


