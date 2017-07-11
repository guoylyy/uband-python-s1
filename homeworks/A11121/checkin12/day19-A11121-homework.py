#!/usr/bin/python
# -*- coding: utf-8 -*
#author: Jinxiao

class examination():
	"""docstring for examination"""
	def __init__(self, name, subject):
		
		self.name = name
		self.subject = subject

	def review(self):  #千万不要忘了要打self！ 这属于对该函数变量的声明？调用？
		print '%s正在复习 %s科目的考试'% (self.name,self.subject)
	def success(self,score):
		print '%s顺利通过了 %s科目的考试，考了%d分'%(self.name,self.subject,score)#好吧经过重新测试，又可以使用%d了，可能只是系统抽了一下吧
	def fail(self,score):
		print '%s在 %s科目的考试中考了%d分，挂了'%(self.name,self.subject,score) #在这里为什么分数是作为str来输入的呢？一旦输入%d就会报错，%s就没事儿
	def tryagain(self):
		print '%s进行了 %s科目考试的补考'%(self.name,self.subject)

def main():
	May = examination('May', 'Physics')
	May.review()#作为一次调用，不要忘了()
	May.success(98)
	May.fail(59)
	May.tryagain()


if __name__ == '__main__':
	main()
		