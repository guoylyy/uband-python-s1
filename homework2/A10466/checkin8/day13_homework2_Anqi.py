#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
  tup = (1,2,3,4)
  try:
    tup.append(2)
    pass
  except Exception, e:
    print '发生错误'
  
if __name__ == '__main__':
  main()
