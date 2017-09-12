#!/usr/bin/python
#-*- coding: utf-8 -*-
#@author:suancaiyu
#学习内容：列表：list 分支判断：for
#01)list: 可以将存放多个对象(包括字符串，数字，)的数据结构，避免用多个变量存放。那么列表可以存放
#  另外一个列表吗?
#02)for:可以逐一的使用列表的每一个对象，当同一相似的动作需要多次使用时利用循环
#03)pass 语句
def main():
      list = ['dabaicai','kongxincai','huacai','shengjiang','xiaolongxia',9,2.3]
      print(list)
      for item in list:  #输出列表中的全部元素
          print item
      list01 = list + ['apple','banana','rice'] #往列表中添加元素的操作
      print list01
      pass #python 中pass 表示什么也不做
      print list01[0] # 打印列表的第0个元素？ 列表中的元素是有序还是无序的？取得列表中某一个值。
      print list01[-1]
      pass
      for item01 in list01:
          print item01
#      list02 = list01 - ['apple','rice'] #列表支持删除操作吗？
  
#      for item02 in list02:
#          print item02
  
if __name__=='__main__':
      main()
