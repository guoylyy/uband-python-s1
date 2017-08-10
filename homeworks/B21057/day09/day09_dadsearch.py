# -*- coding: UTF-8 -*-  
#author fangcheng



def main():
  dictionary = {
               'abandon':'to give up to the control or influence of another person or agent',
               'abase':'to lower in rank, office, prestige, or esteem',
               'abash':'to destroy the self-possession or self-confidence of'
	           }
  print len(dictionary)
  print '老爸在看一本英文书，他旁边有一个词典，但是只有三个词的解释。' 
  print dictionary
  if not dictionary.has_key('etiquette'): #没有查到  只能if true
    print '老爸没有查到 %s 的意思' % ('etiquette')  #print里输出'xx'内容需要将其转换成%s传输字符
  del dictionary['abandon']
  print dictionary
  print '老爸怒了，把含有 %s 一页的单词撕掉了'%('abandon') 
  if dictionary.has_key('abase'):
	print '然后老爸又查了一个单词 %s 得到了解释' %('abase')
	dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
	print dictionary
	print '老爸很开心，有把 %s 加入到了字典里' %('abandon')
if __name__ == '__main__':
  main()