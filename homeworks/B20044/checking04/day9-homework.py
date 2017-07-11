#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业1:对照 day9 sample-code 打一遍代码
#
# 
def homework1():
  #定义
  dictionary = {'good':'of a favourable character or tendency', #中间有=号
  				'none':'not any such thing or person',
  				'nice':'very beautiful'
  				}

  	#长度		有3个元素
  print len (dictionary)

  print dictionary #后面+.  或者是加()都会不能运行   说明当后面有某个具体部分时才要 dictionary._____  ()

  #获取所有keys 有多少个可以查的词 
  print dictionary.keys() #获取key的列表  #记得+（）到底是哪些keys呢？

  #获取所有value
  print dictionary.values() #获取values的列表

  #词典里有没有这个单词→有没有这个key
  print dictionary.has_key('good')#有
  print dictionary.has_key('bad')#没有   中间记得有一个.

  #add增加词（加也是加上含义）
  dictionary['bad']='not very good'  #dictionary['bad']表示取值，也就是它的value=‘’
  print dictionary  #后面+.  或者是加()都会不能运行   说明当后面有某个具体部分时才要 dictionary._____  ()
  print len (dictionary)

  #对内容修改modify，完善   与增加的形式很类似
  dictionary['bad'] = 'failing to reach an acceptable standard'
  print dictionary
  #添加和修改是一个道理，字典里面的每个key是唯一的。当你去添加一个没有的词的时候就是添加，
  #用添加的语法又加一个值的时候，就会把原来的语法覆盖掉。+一个新的bad时会把原来的挤掉。
  
  #删除delete→key和value都没有了   注意：删不是删词key，而是删掉value含义
  del dictionary['bad']
  print dictionary
  print len (dictionary)

 #取值 get value  →  dictionary['key']
  print '--------'
  print dictionary['good']

 # print dictionary['bad']不要访问它没有的值,否则会报错

  if dictionary.has_key('bad'):#查一下是否有这个词，有的话再print出来 中间漏掉.就不能执行  
  	  print dictionary['bad']#没有的话，这一段没办法执行，就不会报错，只会执行else的部分
  else:
  	  print '没有bad这个词'

 #for循环  怎么遍历字典里面的项 iterator  迭代程序
#知道了如何获得它的所有的key→print dictionary.keys()
#也知道如何去取值value 得到解释→ print dictionary['word']
#所以就知道如何遍历所有的key
  for key in dictionary.keys():  #?为什么要加（）
  #→ for lst_item in lst: 我感觉这里的lst就相当于dictionary，后面不用+（）
  #而这里是keys，就如前面一有keys/values ， dictionary的后面就要+  .keys()一样

  	  print key  #不要+s  与上一行相同
  	  print dictionary[key]#这样既获得key又获得value





#作业2: （选做）模拟下面的过程，用今天学到的知识
#【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agent”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到   →has_key
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了  →没有理解撕掉的真正含义是delete
# 然后老爸又查了一个单词 'abase' 得到了解释  →has_key
# 老爸很开心，有把 'abandon' 加入到了字典里   →add增加含义

#总结：2.4没有写出来
       #名称的时候用%s表示，后面（）内要加""

def homework3():
  print '========'
  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释  '
  dictionary= {'abandon': 'to give up to the control or influence of another person or agent',
  			 'abase': 'to lower in rank, office, prestige, or esteem',
  			  'abash': 'to destroy the self-possession or self-confidence of'
  			  }
  if dictionary.has_key('etiquette'):
  	print'老爸查到了%s的意思'%('etiquette')

  else:
  	print'老爸没有查到%s的意思'%('etiquette')

  	del dictionary['abandon']
  	print '老爸撕掉含有%s的那一页 '% ('abandon')
  	#print dictionary.keys ()
  	
  	if dictionary.has_key('abase'):
  		print'老爸查到了%s:%s的解释'%('abase',dictionary['abase'])#不用照抄解释，用取值的方式

  		dictionary['abandon']='to give up to the control or influence of another person or agent'
  		print '老爸把%s的意思加回到字典里。'%('abandon')


  	else:
  		print '没有查到%s的意思'%('abase')









def homework2():
  print '------'

  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释  '
  dictionary= {'abandon': 'to give up to the control or influence of another person or agent',
  			 'abase': 'to lower in rank, office, prestige, or esteem',
  			  'abash': 'to destroy the self-possession or self-confidence of'
  			  }
  			  #漏了中间的=号
  for key in dictionary.keys():
  	print key
  	print dictionary[key]


  if dictionary.has_key('etiquette'):  #蜀黎的代码是直接if not :
  	print dictionary['etiquette']
  else:
  	print "老爸先查了一个单词 'etiquette' 没有查到"  #蜀黎的代码从一个上升到整体，用了%s来泛指→通用

    #要注意，这里的etiquette的位置应该是一个变量，不应该永远都是这个词
  	print "老爸怒了，把含有 'abandon'一页的单词撕掉了" #若两边都是单引号，中间的单词显示为白体，出错

  	#没有真正理解撕掉abandon的含义→这意味着这个词delete掉了。

  	#我把这些代码分块了，但实际上它是按顺序进行的，应该在一个代码块里面。

  if  dictionary.has_key('abase'):
  	print 'abase'
  	print dictionary['abase']
  	print  "然后老爸又查了一个单词' abase '得到了解释"
  	print " 老爸很开心，有把 'abandon' 加入到了字典里  "
  	#不理解加入字典的真正含义 












if __name__ == '__main__':
  homework1()
  homework2()
  homework3()