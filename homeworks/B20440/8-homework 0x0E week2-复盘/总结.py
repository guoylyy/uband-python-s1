#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

#第一周总结
#学习内容：def main(): if __name__ == '__main__'：main()
#return
  #def buybuybuy():……
   # return is_cheap, buy_amount, good_price #作用1：传递变量给调用方 #作用2：返回，不继续执行
  #def main():
   # is_cheap, buy_amount, good_price = buybuybuy()#从buy函数传到main函数
#出现的问题：1.空格问题，注意统一；2.注意缩进（例if，else）；3.单一职责还没有理解透彻；

#week 2（day 10）
#1.明确所定义函数用途，通过定义参数可使代码利用率提高；
#2.注意单一职责原则
#刚开始不会处理作业要求4”如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词“
# 没仔细看第二个版本，所以刚开始不太理解
  #之前的语句处理的是定义字典，管的是谁查什么单词，没查到就撕哪一页，查到新的又黏回去。
  #之后的语句是管打印查到的词和意义，感觉走完homework2就完了，不会跑到search这组语句啊？
#后面发现自己没注意到return，才意识到search不是本来就有的语法，是定义的。
#3.原来还可以用if not
#4.需要自己打代码和分析才会印象深刻，看容易看懂，但有些语句还是不熟，没有参考，自己打肯定打不出来。