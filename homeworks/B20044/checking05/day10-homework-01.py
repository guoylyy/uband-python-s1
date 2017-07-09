#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又查了一个单词 'abase' 得到了解释
# 老爸很开心，又把 'abandon' 加入到了字典里
# 
# 老爸把字典翻了一遍
#   - 看到%s（单词）:%s(意思)
# 
# 第二个作业我已经做完，先不要看第二个版本





# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码    
     #7处→改完后1处      
     

# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码   
#      7处  (注意：撕毁的变成abase→黏贴也变成abase)
#      改完后2处


# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串 释意   →撕掉abase→加入abase(加入时要重新输入释义)
#意思是怎么使 再把abase加入字典时，book ['abase'] = 'to lower in rank, office, prestige, or esteem'这一串可以不写
#？ 
#因为重复了，所以给它设一个标签 tear_word


# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
#     6处
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）


def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }

  #who = '老爸'               加上标签   
  #tear_word = 'abandon'      加上标签      可能会被撕毁的页的key（单词） 

  print '老妈在看一本英文书 ' #%s %(who)换成标签



  if not book.has_key('etiquette'): 
    print '老妈没有查到 %s 的意思' % ('etiquette')   
# if not search  ('etiquette', book, who):   2句话变1句话 → 简洁

#注意：之前误解了，以为这句话本身就有这个功能，但实际上不是。
# 而是在后面定义了一个serch函数后，这里才可以调用，print出老妈没有查到这个词的意思
#因为要反复查询有没有这个词，然后print出查到与否，所以这样重复的操作我们就给它定义了一个函数

    #tear_mean = book[tear_word]         加上这句话   tear_mean指一长串的单词含义→标签   tear_word是上面已知的

    #撕毁了abandon   因为后面还要贴回来，所以重复了，所以给它设标签
    del book['abase']#1   注意：删不是删词key，而是删掉value含义
   #del book [tear_word]   所以在一开始，就要先定义tear_word这个变量 = 哪个单词

    print '老妈撕毁了 %s 的页面 ' % ('abase')#2   改成 (who,tear_word)



    if book.has_key('abandon'):#换成abandon   5
      print '老妈查到了 %s :%s ' % ('abandon', book['abandon']) #6.7

#   if search ('abandon',book ,who):         2合1

  
      #老爸黏贴了代码（又得重新写一长串的解释，所以如何免除？）
      book ['abase'] = 'to lower in rank, office, prestige, or esteem'#黏贴的必定是abase 3   
      #book[tear_word] = tear_mean   
      #book[tear_word]则表示具体某单词的含义    指的是tear_word后面一长串的释义  因为在book里已有，所以重复了→设标签tear_mean
      #所以要回到前面＋tear_mean这个标签

      print '老妈把 %s 的字典页又贴上了' % ('abase')#4  (who,tear_word)

    else:
      print '老妈没有查到 %s ' % ('abase') 

  else:
    print '老妈查到了 %s '% ('etiquette')


#def search(key,book, who):   #注意后面还有()里的内容  它不是独立开来专门在这里代词搜索的，而是调用的一个函数，像之前day 6作业的print函数一样

  if book.has_key('abase'):#()内加引号    (key)
    print '老妈查到了 %s : %s'%('abase',book['abase'])  #(who, key, book[key])
  # return True   (加上)


  if book.has_key('abash') :
    print '老妈查到了 %s : %s'%('abash',book['abash'])



#再加上下面的
 # else:
    #print '%s 没有查询到 %s 的意思' %(who, key)
    #return False


    

def homework1():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  print '老爸在看一本英文书 '
  if not book.has_key('etiquette'): #没有查到→用的是if not的形式
    print '老爸没有查到 %s 的意思' % ('etiquette')   #注意()里要加'',否则不能运行

    #撕毁了abandon
    del book['abandon']
    print '老爸撕毁了 %s 的页面 ' % ('abandon')#不是直接写abandon，而是用%s表示

    if book.has_key('abase'): #注意缩进，它是这样顺序下来的，所以还是在这个代码块内    查到了就用if
      print '老爸查到了 %s :%s ' % ('abase', book['abase']) #注意中间是key与value之间是冒号。其实其他符号也可以。
      #注意，可以写成  单词： 解释   的形式

      #老爸黏贴了代码
      book['abandon'] = 'to give up to the control or influence of another person or agent'
      print '老爸把 %s 的字典页又贴上了' % ('abandon')

    else:
      print '老爸没有查到 %s ' % ('abase') 

  else:
    print '老爸查到了 %s '% ('etiquette')


if __name__ == '__main__':
  homework1()
  homework2()