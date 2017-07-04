# -*- coding: utf-8 -*-

def homework2():
  who = 'Mom'
  dictionary = {
    'abandon': 'to give up to the control or influence of another person or agent',
    'abase': 'to lower in rank, office, prestige, or esteem',
    'abash': 'to destroy the self-possession or self-confidence of'
  }
  length = len(dictionary)
  key = 'etiquette'
  del_word = 'abandon'

  print '%s looks up a dcitionary with only %d vocabularies' % (who, length)

  print "%s looks up for %s" % (who, key)
  if not dictionary.has_key(key):
    del dictionary[del_word]
    print "There is no %s. %s is mad and deletes the word %s" % (del_word, who, del_word)

  print "%s looks up for %s" % (who,'abase')
  if dictionary.has_key('abase'):
    print 'It means %s' % (dictionary['abase'])
    dictionary["abandon"] = "to give up to the control or influence of another person or agent"
    print "%s is happy so %s re-pastes %s into the dictionary" % (who, who, del_word)

if __name__ == '__main__':
  homework2()