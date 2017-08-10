#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx


def main():
	lst=['apple','orange','banana','lemon']#列表-数组
	#print lst

	for lst_item in lst:#遍历
		print lst_item
		print 'mom see %s'%(lst_item)

if __name__ == '__main__':
	main()
#list:把很多数据放到一个表里，因为这些数据会有同样的操作，所以放在一个列表里一起操作就会比较方便。
#for in 循环就是一个一个地访问列表里的值
#一个一个这个概念，我还要理解，因为呢，我print了两个，但是它却是一个一个地输出的。
#并不是apple orange banana lemon，再是妈妈看到了apple ....而是一个一个输出的，很神奇。
#为了接下来少出Bug，之后的代码我尽量用我的半桶水英文来替换同意思的中文。