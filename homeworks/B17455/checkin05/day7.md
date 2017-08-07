#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

Day7_week1 复盘
1）整理目前学到的东西  
Python中的变量类型：'number', 'string', 'boolean' 【数字型，字符串型，布尔型（只能是 True 或是 False）】
条件判断：if 【根据后面的判决结果是否符合来决定后续语句的执行】
各种变量之间的比较和运算符号： > < ==  >= <= != + - * / %

'--------------------------------------------'
单一职责原则 one file multiple function (code block)
参数传递
#return (pass variable)
#return mutiple variables

代码直接的逻辑关系 e.g. if语句添加位置等等
'--------------------------------------------'
列表lst['太阳', '月亮', '星星']
  # 循环访问
  for lst_item in lst:  #遍历
    # print '老妈看到了 %s '% (lst_item)
    pass
  # 记录下标
  index = 0
  for lst_item in lst:  #遍历
    # print '老妈看到了 %s '% (lst_item)    
    # print '当前第 %d 个' %(index)
    index = index + 1
  # 迭代访问
  for index,lst_item in enumerate(lst):
    # print '老妈看到了 %s '% (lst_item)    
    # print '当前第 %d 个' %(index)
    pass
  #取值
  print lst[0]
  #长度
  print len(lst)
  #加单个元素
  lst.append('白芍')
  print_list(lst)

  #删除
  del lst[0]
  #切片
  lst2 = lst[2:5] # 2,3,4
  print_list(lst2)


2）整理学习所犯的错误以及当时的思维过程  
打代码都要保持英文输入，特别是括号
代码块要注意对齐，缺少缩进
在切片的时候lst[2:5] '：'注意不要打错

3）整理对今后学习有指导意义的方法
逻辑思维清楚真的很重要的！！！
细节小问题错误要根据报错内容查找修改的！