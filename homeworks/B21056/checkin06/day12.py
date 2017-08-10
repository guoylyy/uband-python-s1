#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup
  print tup[0:3]
  print tup[2:]
  
  # 是否存在某值
  print [1 in tup]
  print [5 in tup]


  # 赋值
  a,b,c,d=tup
  print '%s %s %s %s'%(a,b,c,d) 
  print '---------'
  # 遍历
  for item in tup:
    print item
  print '---------'
  for index,item in enumerate(tup):
    print index
    print item

  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除

    #tup.append(9)-------SyntaxError: invalid syntax
    #del tup[0]----------SyntaxError: invalid syntax
    tup[0]='aaa'--------SyntaxError: invalid syntax
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()


