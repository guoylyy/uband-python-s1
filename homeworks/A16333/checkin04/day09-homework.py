#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

#作业1
def main():
  dictionry ={
               'good':'of a favorable character or tendenc',
               'none':'not any such thing or person',
               'nice':'very beatiful'

              }
  print len(dictionry)#长度
  print dictionry.keys() #获取key的列表
  print dictionry.values() #获取value的列表

  #是不是在
  print dictionry.has_key('good') #有
  print dictionry.has_key('bad') #没有

  #添加
  dictionry['bad']= 'not very good'
  print dictionry.keys()

  #modify
  dictionry['bad']= 'failing to reach an acceptable standard'
  print dictionry

  #delete
  del dictionry['bad']
  print dictionry
  print len(dictionry)

  #get value
  print '-----'
  print dictionry['good']
  if dictionry.has_key('bad'):
  	print dictionry['bad']
  else:
  	print '没有bad这个单词 '
  print '-----'


 #iterator
  for key in dictionry.keys():
    print key 
    print '-----'
    print dictionry.keys()
#作业2：【场景模拟】
#
# 老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释
# abandon “to give up to the control or influence of another person or agen”
# abase  “to lower in rank, office, prestige, or esteem ”
# abash  “to destroy the self-possession or self-confidence of ”
# 
# 老爸先查了一个单词 'etiquette' 没有查到
# 老爸怒了，把含有 'abandon' 一页的单词撕掉了
# 然后老爸又差了一个单词 'abase' 得到了解释
# 老爸很开心，有把 'abandon' 加入到了字典里
def daddy():
  print '---作业2-----'
  dictionary = {
                'abandon':'to give up to the control or influence of another person or agen',
                'abase':'to lower in rank, office, prestige, or esteem ',
                ' abash':'to destroy the self-possession or self-confidence of'
                 }
  #print dictionary
  if dictionary.has_key('etiquette') is True: #想不明白为什么通过呢？
    pass
  else:
    print '老爸先查了一个单词 "etiquette"没有查到 '
    print ' 老爸怒了，把含有 "abandon" 一页的单词撕掉了  '
    del dictionary['abandon'] 
  	
  if dictionary.has_key('abase') is True:
  	print '然后老爸又差了一个单词 "abase"得到了解释 '
  	print "老爸很开心，有把 'abandon' 加入到了字典里"
  	dictionary['abandon']='to give up to the control or influence of another person or agen'
  else:
  	pass




if __name__ == '__main__':
	main()
	daddy()