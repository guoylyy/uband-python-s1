#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan
def print_list(lst):
  for lst_item in lst: #遍历
  	print '老妈看到了%s '% (lst_item)


def main():
  #       0           1        2       3       4
  lst = ['大白菜 ','空心菜 ','花 菜','生姜 ','小龙虾 ']#列表
  # 循环访问
  for lst_item in lst: #遍历
    print '老妈看到了%s '% (lst_item)
# 记录下标
  print '--1---'
  index = 0
  for lst_item in lst:
  	print '老妈看到了%s '%(lst_item)
  	print '当前第%d 个' %(index)
  	index = index + 1
# 迭代访问
  print '--2---'
  for index, lst_item in enumerate(lst):
  	print '老妈看到了%s ' %(lst_item)
  	print '当前第 % d 个 ' % (index)

# 取值
  print'__3___'
  print lst[0] 
  print lst[1]
# 长度
  print  len(lst)
# 加
  lst.append('白芍')
  print_list(lst)
# 删除
  del lst[0]
  print '--4--'
  print_list(lst)
# 切片
  lst2 = lst[0:3] # 0,1,2
  print lst2
  for item in lst2:
    print item

if __name__ == '__main__':
	main()

