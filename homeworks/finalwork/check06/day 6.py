#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小八
def print_list(lst):
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

def main():
  #       0         1        2        3       4
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾'] #列表
  # 循环访问
  for lst_item in lst:  #遍历
    # print '老妈看到了 %s '% 
  

  # 记录下标
index = 1
  for lst_item in lst:  #遍历
    # print '老妈看到了 %s '% (lst_item)    
    # print '当前第 %d 个' %(index)
    index = index + 1

  # 迭代访问
  for index,lst_item in enumerate(lst):

  print lst[0]
  print len(lst)
  
  lst.append('')
  print_list(lst)

  #删除
  # del lst[0]
  print '---'
  # print_list(lst)

  #切片
  lst2 = lst[2:5] # 2,3,4
  print_list(lst2)

def main2():
  # 记录下标
  index = 0
  for lst_item in lst:
    print lst_item
    print '第 %d 个' % (index)
    index = index + 1

  # 迭代
  for index,lst_item in enumerate(lst):
    print index
    print lst_item
  #取值
  print lst[0]
  #长度
  length = len(lst) #5
  print '该列表有 %d 个元素' % (length)
  
  #加
  lst.append('意面')
  length = len(lst) #6
  print '该列表有 %d 个元素' % (length)

  #删除
  del lst[0] #删除
  #切片
  lst2 = lst[1:4] #0,1,2

  print lst2
  for item in lst2:
    print item


if __name__ == '__main__':
  main()