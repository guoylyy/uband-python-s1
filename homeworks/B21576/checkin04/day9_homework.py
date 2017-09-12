#!/usr/bin/python
#-*-coding:utf-8-*-
#@author:suancaiyu
#学习内容： 字典的操作  添加，删除，求字典长度，
def main():

	dictionary = {

                'abandon': 'to give up to the control or influence of another person or agent',
                'abase': 'to lower in rank, office, prestige, or esteem',
                'abash': 'to destroy the self-possession or self_confidence of'
               }
	print '老爸在看一本英文书，他旁边有一个词典，但是只有%d个词的解释' %(len(dictionary))
  
	print '老爸查了一个单词 etiquette'

	if dictionary.has_key('eqtiquette'):
		print dictionary ['eqtiquette']
	else:
		print '没有查到'
  
  #老爸生气撕字典
	print '老爸怒了,撕掉了abandon的那页'

	del dictionary['abandon'] 
	print '字典里只剩下 %d 个词' % (len(dictionary))

  #再查单词
	print '然后老爸又查了一个单词 abase'

	if dictionary.has_key('abase'):
		 print dictionary['abase']
  
  #老爸很开心又再粘字典
	print '老爸很开心，又把abandon加入了字典'

	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'

	print '字典里有 %d 个词' % (len(dictionary))



if __name__ == '__main__':
	main()
