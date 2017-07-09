#!/usr/bin/python
# -*- coding: utf-8 -*-

#homework1
def homework1():
  week_overnight=[False, False, True, False, False]

  for index,is_overnight in enumerate(week_overnight):
  	index=index+1
  	print "今天星期%d "% (index)

  	try:#注意try的缩进，它是属于for函数里面的 遍历完再try一下
  	  overnight_check(is_overnight)
  	except Exception,e:
  	  print "发生错误:%s"%(e)


def overnight_check(is_overnight):
  if is_overnight:
  	raise Exception('离婚')
  else:
  	print '正常 '   


#homework2
# 构思：上面是def over_night夜不归宿中止程序，然后try的时候改为不让中止程序，只是报错
#       所以这里def search 字典查不到词中止程序，然后try的时候改为不让中止程序，只是报说查不到词

def search(dic,key):
  print '我在查找单词%s'%(key)

  if dic.has_key(key):
    print '%s:%s'%(key,dic[key])
  else:
    raise Exception('字典里没有这个词')

def homework2():
  dic = {
                'good':'of a favorable character or tendency',
                'none': 'not any such thing or person',
                'nice': 'very beautiful'
               }


  try:
    search(dic,'okay')
    
  except Exception as e:
    print '发生错误:%s'%(e)
 


  

if __name__ == '__main__':
  homework1()
  homework2()