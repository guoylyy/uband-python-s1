#!/usr/bin/python
#filename:day9practice.py

def main():
    dictionary = {'abandon':'to give up to the control or influence of another person or agent','abase':'to lower in rank, office, prestige, or esteem','abash':'to destroy the self-possession or self-confidence of'}
    print 'my dad was looking at a dictionary with explanations of three words'
    print dictionary
    if dictionary.has_key('etiquette'):
      print "my dad checked the meaning of 'etiquette'"
    else:
      print "my dad was really angry,he tore the page with 'abandon'on it"
    del dictionary['abandon']
    print dictionary
    print 'my dad looked up another word,abase,he found the word,abase'
    print dictionary['abase']
    
    print 'my dad was really happy, he put that page back'
    dictionary['abandon']='to give up to the control or influence of another person or agent'
    print dictionary
if __name__ == '__main__':
  main()


