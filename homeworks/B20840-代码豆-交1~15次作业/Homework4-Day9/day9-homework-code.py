#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

def homework1():
	#定义这个字典里面的内容
	dictionary = {'abandon':'to give up to the control or influence of another person or agent',
					'abase':'to lower in rank, office, prestige, or esteem',
					'abash':'to destroy the self-possession or self-confidence of'
					}
	print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释，他们分别是%s' %(dictionary)
	print '==========================='
	#老爸准备撕书了
	if dictionary.has_key('etiquette'):
		print dictionary
	else:
		del dictionary['abandon'] #就是在这里撕书的
		print '老爸怒了，把含有’abandon‘一页的单词撕掉了'
		print '现在字典里面只剩下了%s' %(dictionary.keys())
	print '==========================='
	#老爸准备开心了
	if dictionary.has_key('abase'):
		print '老爸得到了abase这次词的解释是%s' %(dictionary['abase'])
		dictionary['abandone']='to give up to the control or influence of another person or agent' #把abandon添加回去了
		print '老爸很开心，又把’abondon‘加入到字典里面了'
		print '现在字典里面有三个词的解释，你看%s' %(dictionary)




if __name__ == '__main__':
	homework1()