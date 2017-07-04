#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

#作业1:对照 day9 sample-code 打一遍代码
#
print 'homework1'
def homework1():
    dic1 = {
    'good':'of a favorable character or tendenc', 
    'none': 'not any such thing or person', 
    'nice': 'very beautiful'
    }
    print dic1

    print '#长度'
    print len(dic1) 

    print '#获得keys'
    print dic1.keys()

    print '#获得value'
    print dic1.values()

    print '#是不是在'
    print dic1.has_key('good') #在
    print dic1.has_key('bad') #不在

    print '#add'
    dic1['bad'] = 'not good'
    print dic1

    print '#modify'
    dic1['bad'] = 'likely to cause major problems'
    print dic1
  
    print '#delete'
    del dic1['none']
    print dic1

    print '# get value'
    print "value of key 'good' in dic1:",  dic1['good']
    if dic1.has_key('stupid'):
        print "value of key 'stupid' in dic1:", dict1['stupid']
    else:
        print "value of key 'stupid' in dic1:", "#no such word as 'stupid'"

    print '# iterator'
    for key in dic1:
        print key
        print dic1[key]

if __name__ == '__main__':
    homework1()

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
print ' '
print 'homework2'
def homework2():
    dic2 = {
    'abandon':'to give up to the control or influence of another person or agent', 
    'abase':'to lower in rank, office, prestige, or esteem ',
    'abash':'to destroy the self-possession or self-confidence of'
    }
    print "Dad's reading an English book. Beside him was a dictionary with only three words on it:"
    for key in dic2:
        print key
        print dic2[key]
    print '---'
    print "Dad, without knowing it, looked up the word 'etiquette', and got no result"
    print "Furious, he tore up the page with the word 'abandon' on it"
    print "Then he looked up another word 'abase', getting its explanation:", dic2['abase']
    print "Dad was so happy that he added the word 'abandon' back to the dictionary"

if __name__ == '__main__':
    homework2()

print ' '
print 'homework2-2.0'
def homework2_2():
    dic3 = {
    'abandon':'to give up to the control or influence of another person or agent', 
    'abase':'to lower in rank, office, prestige, or esteem ',
    'abash':'to destroy the self-possession or self-confidence of'
    }
    print "Dad's reading an English book. Beside him was a dictionary with only three words on it:"
    for key in dic3:
        print key
        print dic3[key]
    print '---'
    print "Dad, without knowing it, looked up the word '%s'," % ('etiquette')
    if not dic3.has_key('etiquette'):
        print "and got no result (of the word '%s')" % ('etiquette')
        del dic3['abandon']
        print "Furious, he tore up the page with the word '%s' on it" % ('abandon')

        print "Then he looked up another word '%s'," % ('abase')
        if dic3.has_key('abase'):
            print "getting its explanation: %s" % (dic3['abase'])
            dic3['abandon'] = 'to give up to the control or influence of another person or agent'
            print "Dad was so happy that he added the word '%s' back to the dictionary" % ('abandon')
        else:
            print "and got no result (of the word '%s')" % ('abase')
    else:
        print "and got its meaning: %s" % (dic3['etiquette'])

if __name__ == '__main__':
    homework2_2()