#!/usr/bin/python
# -*- coding: utf-8 -*-

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
def Find(word,dic):
    who = '蜀黍'
    if not(word in dic):
        print (("%s没有查到单词%s")%(who,word))
        del dic['abandon']
        print (("%s怒了，把含有 'abandon' 一页的单词撕掉了")%(who))
    else:
        print (("%s查到单词%s")%(who,word))
        dic['abandon']='to give up to the control or influence of another person or agent'
        print (("%s很开心，有把 'abandon' 加入到了字典里")%(who))
    print(dic.keys())
    print("---")
def homework2():
    dic = {
            'abandon':'to give up to the control or influence of another person or agent',
            'abase' :'to lower in rank, office, prestige, or esteem',
            'abash' : 'to destroy the self-possession or self-confidence of'
            }
    Find("etiquette",dic)
    Find("abase",dic)
   
def homework1():
    dic =   {
            'good' :'好',
            'none': '没有',
            'nice' : '很好'
            }
    
    print (len(dic))
    print (dic.keys())
    print (dic.values())
    
    print ('good' in dic)
    print ('bad' in dic)
    
    #modify
    print('---')
    dic['bad']='好'
    print (dic)
    print ('----')
    dic['bad']='不好'
    print (dic)
    
    
    #delete
    del dic['bad']
    print ('---')
    print (dic)
    
    if 'bad' in dic:
        print (dic['bad'])
    else :
        print ('bad is not in the dict.')
        
    # 遍历
    for key in dic.keys():
        print (key)
        print (dic[key])

if __name__ == '__main__':
  homework1()
  print("")
  homework2()