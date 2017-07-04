#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Carrie

# 3. 想想如何让最后粘贴回 撕毁代码页 的时候不用重复再打一遍长串释意
# 4. 如果查到就打印:'老爸查到了 %s : %s', 写代码让老爸再搜索'abase' 'abash'这两个单词
#    数一数有多少处重复的打印代码
# 
# 做完这些过后，打开 day10-homework2.py 做同样的事情（3除外）
def homework2():
  dictionary = {
    'abandon': 'to give up to the control or influence of another person or agent',
    'abase': 'to lower in rank, office, prestige, or esteem',
    'abash': 'to destroy the self-possession or self-confidence of'
  }
  who = 'Mom'
  length = len(dictionary)
  del_word = 'abandon'

  print '%s looks up a dcitionary with only %d vocabularies' % (who, length)
  if not search('etiquette', dictionary, who):
    action = dictionary[del_word] #magic!!!
    del dictionary[del_word]
    print '%s deletes %s ' % (who, del_word)

    if search('abase', dictionary, who):
      dictionary[del_word] = action #magic!!!
      print '%s re-pastes %s ' % (who, del_word)
      print dictionary.keys()

def search(key, dictionary, who):
  if dictionary.has_key(key):
    print 'There is %s: %s' % (key, dictionary[key])
    return True
  else:
    print 'There is no %s' %(key)
    return False

if __name__ == '__main__':
  homework2()