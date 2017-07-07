#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin


#作业1:对照 day9 sample-code 打一遍代码

def homework1():
	dictionary = {
		          'good': 'a favoritable character or tendenc',
		          'none': 'not any such thing or person',
		          'nice': 'very beautiful'
	              }
	print len(dictionary)    #长度
	print dictionary.keys()   #获得keys的列表 有多少可以查的词   一定注意要加s  keys
	print dictionary.values()  #获得values的列表
	print dictionary.has_key( 'good')   #这个字典有没有这个单词   一定要注意dictionary和 has_key中间加的是点
	print dictionary.has_key('bad')
	
	#字典的话，势必可以增加一个单词
	dictionary['bad'] = 'not very good'	

	print dictionary
	print len(dictionary)
	
	#修改字典条目
	dictionary['bad'] = 'failing to reach an acceptable standard'
	print dictionary
	
	#删除条目
	del dictionary['bad']
	print dictionary
	print len(dictionary)
	
	#for
	print '---'
	print dictionary['good']  #这种方法可以直接用来取值。 一个单词的意思。
	
	if dictionary.has_key('bad'):   #因为上面删除了bad的条目，所以直接print的话是没有的，所以可以先判断一下，是否有这个单词。
	                                #一定不要忘记结尾的冒号。
	  print dictionary ['bad']      #没有的话，这一段不会执行
	else:
	  print '没有bad这个单词'
	print '----'
	
	for key in dictionary.keys():    #获取所有的单词（key）
		print key
		print dictionary[key]

	

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
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里
# 


def homework2():
  dictionary = {
                'abandon': 'to give up to the control or influence of another person or agent',
                'abase': 'to lower in rank, office, prestige, or esteem',
                'abash': 'to destroy the self-possession or self_confidence of'
               }
  print '老爸在看一本英文书，他旁边有一个词典，但是只有%d个词的解释' % (len(dictionary))
  
  print '老爸查了一个单词 etiquette'

  if dictionary.has_key('eqtiquette'):
    print dictionary ['eqtiquette']
  else:
  	print '没有查到'
  
  #老爸生气撕字典
  print '老爸怒了,撕掉了abandon的那页'

  del dictionary['abandon'] 
  print '字典里只剩下 %d 个词' % (len(dictionary))

  #再查单词
  print '然后老爸又查了一个单词 abase'

  if dictionary.has_key('abase'):
    print dictionary['abase']
  
  #老爸很开心又再粘字典
  print '老爸很开心，又把abandon加入了字典'

  dictionary['abandon'] = 'to give up to the control or influence of another person or agent'

  print '字典里有 %d 个词' % (len(dictionary))



if __name__ == '__main__':
  homework1()
  homework2()