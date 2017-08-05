#!usr/bin/python
#-*- coding:utf-8 -*-

def main():
  tup = (1,2,3,4)

  #取值
  print tup[0]
  print tup[1]
  print tup[2]
  print tup[3]

  # 切片
  print tup[1:3]
  
  # 是否存在某值
  print (1 in tup)
  print (5 in tup)
  print ('ss' in tup)

  # 赋值
  a,b,c,d=tup
  print a
  print b
  print c
  print d
  # 遍历
  print "------遍历--------"
  for item in tup:
  	print item


  # 花式报错
  # 不支持 1)插入 2)修改 3) 删除
  try:
    # tup.append('4')
    # tup[2]=3
    del tup[2]
  except Exception, e:
    print e
  
if __name__ == '__main__':
  main()