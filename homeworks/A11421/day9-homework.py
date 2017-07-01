#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#作业1:对照 day9 sample-code 打一遍代码
#
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
def homework1():
  dic = { 
   		"abandon":"to give up to the control or influence of another person or agent",
   		"abase":"to lower in rank, office, prestige, or esteem",
   		"abash":"to destroy the self-possession or self-confidence of"
   		}
  word1 = "etiquette"
  word2 = "abandon"
  word3 = "abase"
  who = "老爸"

  print "%s在看一本英文书，他旁边有一个词典" % (who)

  if not search(word1, who, dic):
    print "%s怒了，把含有 %s 一页的单词撕掉了" %(who, word2)
    
    del_word = dic[word2]
    del dic[word2]

    if search(word3, who, dic):
      print "%s很开心，又把 %s 加入到了字典里" % (who, word2)
      dic[word2] = del_word


def search(word, who, dic):
  if dic.has_key(word):
    print "%s查到了 %s，意思是 %s " % (who, word, dic[word])
    return True
  else:
    print "%s查了一个单词 %s 没有查到" % (who, word)
    return False
 

if __name__ == '__main__':
  homework1()