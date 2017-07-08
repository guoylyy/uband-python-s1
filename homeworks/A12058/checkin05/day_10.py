# -*-coding: utf-8 -*-
# @author: Shuan

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
print 1

def main():
  dictionary={
              'abandon' : 'to give up to the control or influence of another person or agent',
              'abase' : 'to lower in rank, office, prestige, or esteem ',
              'abash': 'to destroy the self-possession or self-confidence of '
              }
  print '老爸在看一本英文书'
  if not dictionary.has_key('etiquette'):
    print '老爸没有查到%s的意思 '%('etiquette')

    del dictionary['abandon']
    print '老爸撕毁了%s的页面 '%('abandon')

    if dictionary.has_key('abase'):
     print '老爸查到了%s的意思 '%('abase')
     dictionary['abandon']='to give up to the control or influence of another person or agent'
     print '老爸把 %s 的字典页又贴上了 '%('abandon')
    else:
      print '老爸没有查到%s的意思 '%('abase')
  else:
  	print '老爸查到了%s的意思 '%('etiquette')
  

if __name__ == '__main__':
 main()


# 做几件事情
# 1. 把老爸换成老妈，做的时候数一数改了几处代码
# 2. 把撕毁的页码换成'abase'，做的时候数一数改了几处代码
# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再a搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码

def main():
  dictionary={
              'abandon' : 'to give up to the control or influence of another person or agent',
              'abase' : 'to lower in rank, office, prestige, or esteem ',
              'abash': 'to destroy the self-possession or self-confidence of '
              }
  print '老妈在看一本英文书'
  if not dictionary.has_key('etiquette'):
    print '老妈没有查到%s的意思 '%('etiquette')

    del dictionary['abandon']
    print '老爸撕毁了%s的页面 '%('abandon')

    if dictionary.has_key('abase'):
     a='to give up to the control or influence of another person or agent'
     print '老爸查到了%s的意思 '%('abase')
     dictionary['abandon']=a
     print '老爸把 %s 的字典页又贴上了 '%('abandon')
    else:
      print '老爸没有查到%s的意思 '%('abase')

    if dictionary.has_key('abash'):
     print '老爸查到了%s的意思 '%('abash')
    else:
    	pass
  else:
  	print '老爸查到了%s的意思 '%('etiquette')

if __name__ == '__main__':
 main()


# 1. 7处
# 2. 4处
# 3. 设a='to give up to the control or influence of another person or agent',将第71行改为dictionary['abandon']=a
# 4. 4

def homework():
    book={
        'abandon' : 'to give up to the control or influence of another person or agent',
        'abase' : 'to lower in rank, office, prestige, or esteem ',
        'abash': 'to destroy the self-possession or self-confidence of '
        }
    who = '老爸'
    tear_word = 'abandon'

    print '%s在看一本英文书'%(who)
    if not search('etiquette', book, who):
      tear_mean = book[tear_word]

      del book[tear_word]
      print '%s撕毁了%s的页面'%(who, tear_word)

      if search('abase', book, who):
        book[tear_word]=tear_mean
        print '%s又把%s加上去了'%(who, tear_word)

def search(key, dictionary, who):
	if dictionary.has_key(key):
		print '%s查到了%s：%s'%(who, key, dictionary[key])
		return True
	else:
		print '%s没查到%s的意思'%(who, key)
		return False

if __name__=='__main__':
	homework()
#1. 1处
#2. 1处
#3. tear—main
#4. 0