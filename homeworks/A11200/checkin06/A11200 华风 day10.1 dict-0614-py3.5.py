#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

#作业3: 模拟下面的过程，
#【场景模拟】
# 老妈在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老妈先查了一个单词 'etiquette' 没有查到
# 老妈怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老妈又查了一个单词 'abase' 得到了解释
# 老妈很开心，又把 'abandon' 加入到了字典里
# 
# 第二个作业我已经做完，先不要看第二个版本

# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码: 改名称5处
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码： 修改4次
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意 : 把释义 赋值给一个变量，再让变量赋值给词典。
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码   :  重复搜索2次词典。
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）

def homework3():
  dictionary = {
                'abandon':'to give up to the control or influence of another person or agent',
                'abase':'to lower in rank, office, prestige, or esteem',
                'abash':'to destroy the self-possession or self-confidence of'
               }
  mean_abase = 'to lower in rank, office, prestige, or esteem'
  mean_abash = 'to destroy the self-possession or self-confidence of'
  words = 'abase'
  words1 = 'abash'
  words_no = 'etiquette'
  print ('老妈在看一本英文书，她旁边有一本词典，但只有三个单词的解释，如下：')   #改1
  print (dictionary)
  print ('老妈开始查字典，她想找‘etiquette’这个单词')  #改2
  if ('etiquette' in dictionary.keys()):
    print ('dictionary has %s' % (words_no))
  else :
  	del dictionary['abase']    # 改1.1

  print ('结果老妈没找到‘etiquette’这个单词，她把有‘abase’这个单词的这页斯掉了')  #改3  改1.2
  print (dictionary)

  print ('老妈又开始查字典，他想找‘abase’这个单词')      #改4
  if ('abase' in dictionary.keys()):
    print ('dictionary has %s' % (words))
  else :
  	dictionary['abase'] = mean_abase  #改1.3
  	print(dictionary) 
  print ('结果老妈没有找到了‘abase’这个单词，她又把‘abase’这个单词加到字典中了') #改5  改1.4
  print (dictionary)
  print ('老爸又开始查字典，他想找‘abase’这个单词') 
  if ('abase' in dictionary.keys()):
    print ('老爸查到了 %s ：%s' % (words,mean_abase))
  else :
  	pass
  print ('老爸又开始查字典，他想找‘abash’这个单词') 
  if ('abash' in dictionary.keys()):
    print ('老爸查到了 %s ：%s' % (words1,mean_abash))
  else :
  	pass   
if __name__ == '__main__':
  homework3()