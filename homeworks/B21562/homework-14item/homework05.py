# -*- coding:utf-8 -*-
def xxx():
	a=1
	b=2
	c=a+b
	return a,b,c
def print1(a,b,c):
	print a,b,c
def yyy():
	les=[1,2,3,4,5] #列表也可以不写在主函数里，而是单独建一个函数
	return les  #但是要记得把单独建的列表变量return回主函数里
def print2(les):
	for x in les:
		print x
		return x  #这里return之后就断掉了，不可能继续再循环回去执行
def print3(les):
	for lm,i_n in enumerate(les): #前一个是下标，后一个是内容
		print i_n


def main():
	les=yyy() #主函数里传递刚刚建立的列表函数yyy，说明它的变量为les
	#x=print2(les)
	#print x
	print3(les) #在主函数里执行函数print3（les）中的内容



if __name__ == '__main__':
	main()
