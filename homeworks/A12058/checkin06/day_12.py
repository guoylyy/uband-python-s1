
# -*- coding: utf-8 -*-
# @author: shuan

def main():
  tup = (1,2,3,4)

  #取值
  print tup[1]
  # 切片
  print tup[0:2]
  print tup[2:]
  # 是否存在某值

  print (1 in tup)
  print (5 in tup)
  
  # 赋值
  a,b,c,d = tup
  print a,b,c,d
  # 遍历
  for item in tup:
    print item

  print '---'
  for index, item in enumerate(tup):
    print index

  # 花式报错
  # 不支持 1)插入 
  #tup.append(2)
  #2)修改
  #tup[0]='a' 
  #3) 删除
  #del tup[3]

  try:
    pass
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()