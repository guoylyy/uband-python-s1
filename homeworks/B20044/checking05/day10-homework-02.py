#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 实现了和 homework01 一样的功能
# 供你分析和对比


#笔记：
#学习方法：
#学编程已经进入套路了。打开菜鸟教程的基础教程，一点点地往下看。
#觉得能懂，就开新页面，敲代码。整理错误。
#全部扫完，就可以了。


#1.什么是Don't repeat yourself    (非常有用，但知易行难)
#当某段代码的东西重复了三遍以上，你就很可能可以做一些改进了。(不是一定，因为有些重复是必要的)
#入门时养成好习惯。坏习惯养成后很难改。(负基础 → 掌握了一些知识，但是养成了坏习惯)
#就像学游泳，坏习惯很难改一样。



#笔记：
#1.以后写程序会很频繁地换变量，很容易换错，出问题
#所以  编程要考虑可维护性和变化的情况

#2.变简洁的武器

#1）重复次数多的字符——变量
   #把重复的东西换成变量
   #可以在函数（代码块）里给一段数据贴标签(很好用) →  以后用标签即可   eg.给"老爸"这个数据贴标签who  后面全部用的是标签who

   #当要变数据时，只要把标签贴在另外的数据上就可。  eg.当要把数据变成'老妈'时，把标签who贴在"老妈"上即可

  #所以，变量(左边）的实质就是标签。 可以用在任何地方。要换标签对应的数据时，直接换数据就行。

#2）重复次数多的操作——函数






def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老爸'
  tear_word = 'abandon'      #可能会被撕毁的页的key（单词） →标签

  print '%s在看一本英文书 ' % (who)

  if not search('etiquette', book, who):  #如果后面没有search函数，这里会报错，search没有定义 
  #所以这里的search是调用了后面的函数，使它能够print出来
    tear_mean = book[tear_word]    #tear_mean指撕掉的单词含义→标签

    del book[tear_word] #del book['']
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abase', book, who):
     
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      #book['']='一长串释义'
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)




#工厂是把很多需要重复的东西生产成一个元件 
#比如：流水线上50个元件  不可能只有1个机器就能生产出所有元件，
#否则就相当于一个工匠完成了所有任务，链条式写法
#意思就是不可能一个词一个词地查过来，像昨天的作业一样。

#我们写代码要像工厂的流水线，用一个个单一原则的元件进行工作 —— 不同的机器做单一职责的工作
#这里可以抽出一个代码形成一个单一职责的元件，那里也可以抽出一个；  (有人生产玩具车的头，有人生产尾，各司其职。)
#产品这里加一个元件，那里加一个元件，那里把它修改一下。
#把重复的东西都抽出来变成一个可以生产元件的东西(专门查字典里有没有这个词)


#def search(key, dictionary, who)这个搜索的代码既是单一职责的，又是会不断重复使用的，就能把它生成一个函数
#这相当于工厂流水线上的一个元件


def search(key, dictionary, who):    #注意后面还有()里的内容  因为要调用main函数中的这几个变量，所以要在()里写上
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False




def homework1():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abase' #可能会被撕毁的页的key 改1

  print '%s在看一本英文书 ' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]

    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)


    if search('abandon', book, who):  #改2
      #老爸黏贴了代码
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)


if __name__ == '__main__':
  homework1()
  homework2()
  
  #总结：
  #学代码是从低级到高级，我们可以从很多重复的例子中抽出一个模型来，显得更加高效
  #第二个代码很神奇，比如它可以用if search('abandon', book, who):的形式来生成老妈查询到了abandon的意思，

 #想法错误，并不是它本身就能print出这句话，而是在后面调用了一个search的函数，使他能够print出来。



  #而且给出来的除了单词key之外，还有单词的解释value