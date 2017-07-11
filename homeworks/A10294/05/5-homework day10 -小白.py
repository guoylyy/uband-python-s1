#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老妈'
  tear_word = 'abase' 
  add_word = 'abase'
  print '%s在看一本英文书' % (who)
  if not search('etiquette', book, who):
    tear_mean = book[tear_word]
    del book[tear_word]
    print '%s撕毁了 %s 的页面' % (who, tear_word)

    if search('abash', book, who):
      
      book[tear_word] = tear_mean
      print '%s把 %s 的字典页又贴上了' % (who, tear_word)
    

def search(key, dictionary, who):
  if dictionary.has_key(key):
    print '%s 查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '%s 没有查询到 %s 的意思' %(who, key)
    return False


if __name__ == '__main__':
  main()

#总结：重复的字符可以使用变量对其进行定义
      #重复的操作可以使用函数，减少重复