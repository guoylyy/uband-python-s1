# -*- coding: utf-8 -*-

#1 read file
def read_file(file_path):
  import codecs
  f = codecs.open(file_path, 'r', 'utf-8')
  lines = f.readlines() # read every line in the file 'f'
  all_words = [] # empty list
  for line in lines:
    line = line.strip() # remove special strings at head and end (space by defalt)
    words = line.split(' ') # split sentences by a slicing string ' ', 'words' here as a list of words in each line
    words = split_word(words) # split again by a slicing string '-'
    all_words.extend(words)  # list of words in all lines, by adding up 'words' lists of each line
  return all_words ###1### lists can be returned among functions, but can't be used directly like values!!!

def split_word(words):  # ['aa', 'aaa-bbb-ccc'] => ['aa', 'aaa', 'bbb', 'ccc']
  all_words2 = [] # empty list
  for word in words:
    if '-' not in word:
      all_words2.append(word)
    else:
      lst_splited_word = word.split('-')  #add a value into list
      all_words2.extend(lst_splited_word)  #add another list into list
  return all_words2

#2-1 format word
def format_word(word):  
  fmt = 'abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ' # optimized
  for char in word: # each letter of the word
    if char not in fmt:
      word = word.replace(char, '') # get rid of numbers to remove interferences
  return word.lower() # put the word (after screening) into lowercase

#2-2 format every word in list 'all_words'
def format_all(all_words):
  formatted_words = [] # empty list
  for word in all_words:  # format every word in 'all_words'
    formatted_word = format_word(word) # formatted and lowercased word inherited from function 'format_word'
    if formatted_word:  ### make sure it's not an empty value ''
      formatted_words.append(formatted_word) # recursion
  return formatted_words ###1###

#3 count frequency of each word, to create a dictionary
def count_word(formatted_words):
    counter_dic = {} # empty dictionary
    for word in formatted_words:
      counter_dic[word] = formatted_words.count(word)
      ### or ###
      # if counter_dic.has_key(word):
      #   counter_dic[word] = counter_dic[word] + 1
      # else:
      #   counter_dic[word] = 1
    return counter_dic ###1### so are dictionaries

#4 output into csv
def print_to_csv(to_file_path, counter_dic):
  nfile = open(to_file_path,'w+') #'w+' means clear the file first, readable, writable
  for key in counter_dic: 
    nfile.write('%s, %s\n' %(key, str(counter_dic[key])))
  nfile.close()

def main():
  all_words = read_file('data1/dt01.txt')  # list 'all_words' inherited from function 'read_file()'
  print 'first list\n', 'includes %d unformatted words\n' % (len(all_words))

  formatted_words = format_all(all_words)  # list 'formatted_words' inherited from function 'format_all()'
  print 'formatted list\n' 'includes %d formatted words\n' % (len(formatted_words)) # list of all formatted words

  counter_dic = count_word(formatted_words) # dictionary 'counter_dic' inherited from function 'count_word()'
  print 'counter dictionary\n', 'includes %d words in total\n' % (len(counter_dic)) # [word]

  #sequence words
  # counter_lst = sorted(counter_dic.iteritems(), key = lambda item:item[1], reverse = True) # sorted(iterable,value,reverse)

  print_to_csv('output/test1-dic.csv', counter_dic)

if __name__ == "__main__":
  main()
