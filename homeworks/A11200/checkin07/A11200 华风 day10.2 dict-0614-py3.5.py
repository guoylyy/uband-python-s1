#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng
# 作业4
# 实现了和 homework01 一样的功能： 华风解读 对比
# 感受：1.一些经常会变化的部分 设置为变量，避免以后修改起来 费时费力。
# 2. 一些经常重复操作的 过程尽量 设置为 模块函数，后续可以直接调变量用。避免重复代码
# 3. 词典的keys 和 values 取值可以 赋值，也可以print 出来。 
# 4. 以上方法可以很方便的降低重复工作。不过就是要记住逻辑关系，避免混乱。
def homework4():
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
  who = '老爸'    #对比：人名 设置为变量，可能有多人查阅此词典
  tear_word = 'abandon' #可能会被撕毁的页的key  

  print ('%s在看一本英文书' % (who))
  if not search('etiquette', book, who):    # 新建函数  谁在字典没有找到 ‘单词’
    tear_mean = book[tear_word]             #把 key赋值 到另一个变量 储存

    del book[tear_word]
    print ('%s撕毁了 %s 的页面' % (who, tear_word))

    if search('abase', book, who):
      #老爸黏贴了代码
      book[tear_word] = tear_mean          # 再把变量储存的 key 赋值到 词典
      print ('%s把 %s 的字典页又贴上了' % (who, tear_word))

def search(key, dictionary, who):             # 新建函数 查询 把 key当变量
  if key in dictionary.keys():
    print ('%s 查询到了 %s:%s' % (who, key, dictionary[key]))
    return True
  else:
    print ('%s 没有查询到 %s 的意思' %(who, key))
    return False


if __name__ == '__main__':
  homework4()