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
  if not search_word('etiquette', dictionary):
    del dictionary['abandon']
    print dictionary 
  if search_word('abase', dictionary):
    print dictionary.has_key('abase')
    dictionary['abandon'] = 'to give up to the control or influence of another person or agent'
    print '老爸很开心，又把 %s 加入到字典里了' %('abandon')

def search_word(key, dictionary)
  if dictionary.has_key(key):
    print '老爸查询到了 %s:%s' % (who, key, dictionary[key])
    return True
  else:
    print '老爸没有查询到 %s 的意思' %(who, key)
    return False
if __name__ == '__main__':
  main()