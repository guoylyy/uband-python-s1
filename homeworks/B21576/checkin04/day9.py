#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:suancaiyu
#学习内容：
#1，字典的定义，求字典长度，如何获得字典键列表，值列表，判断字典包含某个键，添加字典中的元素
#2，字典值的修改，添加，删除，取值， 
#3, 作为序列 字典和列表有什么不同呢？


def main():
	dictionary = {
		          'good': 'a favoritable character or tendenc',
		          'none': 'not any such thing or person',
		          'nice': 'very beautiful'
	              }
	print len(dictionary)    #长度
	print dictionary.keys()   #获得keys的列表 有多少可以查的词   一定注意要加s  keys
	print dictionary.values()  #获得values的列表
	print dictionary.has_key( 'good')   #这个字典有没有这个单词   一定要注意dictionary和 has_key中间加的是点
	print dictionary.has_key('bad')
	
	#字典的话，势必可以增加一个单词
	dictionary['bad'] = 'not very good'	

	print dictionary
	print len(dictionary)
	
	#修改字典条目
	dictionary['bad'] = 'failing to reach an acceptable standard'
	print dictionary
	
	#删除条目
	del dictionary['bad']
	print dictionary
	print len(dictionary)
	
	#for
	print '---'
	print dictionary['good']  #这种方法可以直接用来取值。 一个单词的意思。
	
	if dictionary.has_key('bad'):   #因为上面删除了bad的条目，所以直接print的话是没有的，所以可以先判断一下，是否有这个单词。
	                                #一定不要忘记结尾的冒号。
	  print dictionary ['bad']      #没有的话，这一段不会执行
	else:
	  print '没有bad这个单词'
	print '----'
	
	for key in dictionary.keys():    #获取所有的单词（key）
		print key
		print dictionary[key]
if __name__=='__main__':
	main()
