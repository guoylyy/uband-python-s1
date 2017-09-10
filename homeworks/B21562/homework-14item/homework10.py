#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: werewolf

#芦苇的代码
#def print_list(lst):  这一部分代码以函数形式写出来，后面并没有调用到
#	for lst_item in lst:
#		print '%s'%(lst_item)
def print_list():
  lst=['abandon','abase','cat','abash','book']
  
  return lst


def homework2():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word='abase'
  lst=print_list() #在这里给出一个待查询的列表


  print '%s在看一本英文书' % (who)
  for item,lst_item in enumerate(lst):
    mitem=item+1
    print '%s想查询单词%s'%(who,lst_item)
    try:

      if not search(lst_item, book, who): #在这里调用后面的search函数,遍历lst中的item来查询
        tear_mean = book[tear_word]
        del book[tear_word]
        print '%s撕毁了 %s 的页面' % (who, tear_word)
        mlst_item=lst[mitem] #查询下一个单词
        print '%s继续查询%s的意思'%(who,mlst_item)
        
        if search(mlst_item, book, who):
      #老爸黏贴了代码
          book[tear_word] = tear_mean
          print '%s把 %s 的字典页又贴上了' % (who, tear_word)
    except Exception,e:
      print "出错了"

def search(key, dictionary, who):
    if dictionary.has_key(key):
        print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
        return True #这里保留的意义在于可以通过return中断代码的执行，避免又回去执行其他的代码
    else:
        print '%s 没有查询到 %s 的意思' %(who, key)
        return False
    


if __name__ == '__main__':
  homework2()