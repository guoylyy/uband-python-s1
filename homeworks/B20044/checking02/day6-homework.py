#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，
#     遇到偶数的下标就买，买的数量为下标 + 1 斤
#    遇到奇数的下标就不买
#首先奇偶数就要先用数值表现出来→%2==

#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））


#按照第三天的例子， lst这个变量存在于 def main 函数，  如果 def print_list(lst) 函数想使用,那不应该在def main 函数中，写 return lst 吗？
#Answer:你搞混了return和传递的意思。return不是传递的前提，这里仅仅是传递。
#比如你到代码块 a，里面的变量代码块 b无法调用，那么要用return
#但是这里你看，我们其实是在main里直接调用了代码块 print_lst，变量本身就在main里面，传递过去就好了。
#而第三天的例子，是代码块 buy和talk  在代码块 main里面调用，是一个main 里面调用了 2个 函数。
# 这两个函数本来是无法互相share变量的，用了return，中间做了一个中转，就可以了。  （把buy的变量先return回main里面，然后再直接传给talk)
#就像我给你一个苹果，为啥还要return，但是小明给我一个苹果，我给你，小明那边就是return啊


# def print_list(lst)： 括号中也有，但是我们并没有用return来传递，这样的话写个（lst）这个不是没有意义吗？ 
#return是返回，就是说函数1返回会调用方。 
#print_lst(lst)  仅仅是打印，不需要返回数据给调用方哦
#就好像，一个是我给你一块肉，你要返回给我一个青椒肉丝；另外一个是，我给你一块肉，你给你妈看看，不用返回来给我了

#但是你给出去肉的操作就是  def print_lst(lst): 调用时候传的 lst
#它回不回给你青椒肉丝才是 return

#单一职责原则是说只做一件事，和用什么数据作没有关系，这个函数就是作打印列表的事情..这个代码是提供了一个把列表打印出来的功能啦，就做着一件事。
#这个是我之后会讲的一个原则叫 don't repeat yourself. 就是我们会频繁想要打印列表，那么我们就不用每次都写一个for，而是抽成一个单一职责的函数，用它来实现。


#奇偶数   def print_lst 奇数就return true,偶数就return false
#    
# 【提示】：
#   输出结果可能为
#   ‘老妈来到菜市场
#    老妈看到白菜，买了 1 斤
#    老妈继续逛
#    老妈看到xxx, 不买
#    老妈继续逛
#    ...
#   '

def print_list(lst): #只是为了打出来方便而已 只是把列表打印出来而已  要调用到main函数中的lst，所以要写在（）里
  for lst_item in lst:  #遍历
    print '老妈看到了 %s '% (lst_item)

def main ():
	print '作业1'
#          0	  1		  2		 3
	lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	print "老妈来到菜市场。"

	index=0
	for lst_item in lst:

		if index % 2==0:  #记得要缩进 写=不能运行
			print '老妈看到了%s,买了%d斤'%(lst_item,index+1)#注意s 和d的区别
				
		else:
			print "老妈看到%s,不买"%(lst_item)

		print '老妈继续逛'
		
		index=index+1  #这两行是共有的，可以抽出来

#  2. 完成后，用今天的学到的列表知识，加 3 个菜
	print'作业2'

	lst.append('猪蹄')
	lst.append ('排骨')
	lst.append('香菜')
	print_list(lst) #print_lst是最开始的那个def
	print '老妈一共看到了%d个菜'%(len (lst))
    
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜

	print '作业3'

	lst2 = lst [5:10]#：写成了，错。  左闭右开   
	
	index=5  #注意要写5  不要把它写在for循环里，否则就只会循环5,6
	for lst_item in lst2:#后面要加2
	
		if index % 2==0:  #不用缩进，因为没有在for的下面
				
			print '老妈看到了%s,买了%d斤'%(lst_item,index+1)	


		else:
			print "老妈看到%s,不买"%(lst_item)
			
#注意缩进，不要和for平齐，因为是for代码块下的。
		index=index+1  #不要写在if里面，因为这样的话如果是else index就没法+1了
		print '老妈继续逛'

if __name__ == '__main__':
	main()
#这里不用写print_list是因为这只是从main里打印的部分，真正运行的函数其实还是main函数










