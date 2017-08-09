#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt


#自己原来写的有关思考题的蠢蠢的代码：
def main():
	print '老爸在看一本英文书，他旁边有一个词典，有以下单词'
	dictionary={'abandon':'to give up to the control or influence of another person or agent',
				'abase':'to lower in rank, office, prestige, or esteem',
				'abash':'to destroy the self-possession or self-confidence of'}
	print dictionary

	if dictionary.has_key('etiquette'):
		print '老爸顺利查到了etiquette的意思'
	else:
		print '老爸查了没有etiquette这个单词'


	print '老爸怒了，把含有abandon一页的单词撕掉了'	
	del dictionary['abandon']
	print '现在只剩下以下这些单词'
	print dictionary

	print '然后老爸又查一单词abase，得到解释如下:'
	print dictionary['abase']

	print '老爸很开心，又把abandon加到字典里'
	dictionary['abandon']="to give up to the control or influence of another person or agent"
	print dictionary

if __name__ == '__main__':
	main()


#经过各种思考和看老师sample后自己把一些东西改了重新打了一遍的代码，其实清楚许多，虽说不一定完全透彻。
#眠在看傲慢与偏见，途中需要查词。三个词分别是
#application: close attention/diligence
#thereby:because of that 
#singular:strange
#查impertinence没有查到，气得撕毁了singular那一页
#后来查到了thereby，很开心，把singular那一页又贴上了

#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt


def self-practice():
	dictionary={'appplication':'close attention diligence',
				'thereby':'because of that',
				'singular':'strange'}

	who= '眠'
	tear_word= 'singular'

	print '%s正在看傲慢与偏见'%(who)
	if not search('impertinnence',dictionary,who):
		tear_mean= dictionary[tear_word]

		del dictionary[tear_word] 
		print '%s气得撕毁了%s那一页'%(who, tear_word)

		if search('thereby', dictionary, who):
			dictionary[tear_word]= tear_mean

			print '%s很开心的把%s那一页又贴上了'%(who, tear_word)

def search(key,dictionary,who):
	if dictionary.has_key(key):
		print '%s查到了%s:%s'%(who, key, dictionary[key])
		return True

	else:
		print '%s没有查到%s的意思'%(who, key)
		return False

if __name__ == '__main__':
	self-practice()

	#得到结果：
	#雨眠正在看傲慢与偏见
	#雨眠没有查到impertinnence的意思
	#雨眠气得撕毁了singular那一页
	#雨眠查到了thereby:because of that
	#雨眠很开心的把singular那一页又贴上















