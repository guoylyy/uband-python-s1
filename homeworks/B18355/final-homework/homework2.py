#!/user/bin/python
# -*- coding: utf-8 -*-
# 数一数文本中各个词汇出现的次数，输出词汇的出现频率
# 1. 先用 data1/dt01.txt 的文档数据，大概200个单词，实现单词读取的类 WordReader
#    这个类的功能有几个
#    1）从一个路径里读取txt文件
#    2）把txt的文件分割成一个个单词
#    3) 对单词进行统计计数
#    4）排序
#    3）输出csv
import csv
class WordReader:
	def __init__(self):
		pass
		# self.filedir = filedir
		# self.writedir = writedir
	def read_file(self,filedir):
		file_object = open(filedir)
		try:
			all_text = file_object.read()
		finally:
			file_object.close()
		return all_text  #可以返回吗？
	def word_split(self,all_text):
		word_list = all_text.split(' ')
		word_low = []
		for w in word_list:
			word_low.append(w.lower())
		# print word_low
		return word_low
	def word_count(self,word_list):
		word_dict = {}
		for word in word_list:
			if word_dict.has_key(word):
				word_dict[word] += 1
			else:
				word_dict[word] = 1
		# print type(word_dict)
		return word_dict
	def word_sort(self,word_dict):
		# key = word_dict.keys()
		# key.sort()
		value = []
		key =[]
		# for keys in key:
		# 	value.append(word_dict[keys])

		# return key,value
		sorted1 = sorted(word_dict.items(),key=lambda word_dict:word_dict[1])
		sorted1.reverse()
		length = len(sorted1)
		for index in range(0,length):
			key.append(sorted1[index][0])
			value.append(sorted1[index][1])
		return key,value
	def write_csv(self,key,value,writedir):
		cvfile = file(writedir, 'w')
		writer = csv.writer(cvfile)
		length = len(key)
		# print len(value)
		writer.writerow(["Word","Count"])
		for item in range(0,length):
			# pass
			writer.writerows([[key[item],value[item]]])
		# writer.writerow(value)

def read_file2(filedir):
		file_object = open(filedir)
		try:
			all_text = file_object.read()
		finally:
			file_object.close()
		return all_text  #可以返回吗？
def word_split2(all_text):
		word_list = all_text.split(' ')
		word_low = []
		for w in word_list:
			w.strip()
			word_low.append(w.lower())
		# print word_low
		return word_low
def redu(word_dict):
    new_wd ={}
    keys = word_dict.keys()
    
    for items in keys:
        flag = True
        items = items.strip(' ')
        
        for i in range(0,len(items)):
            # if items[i] == '$':
            if (items[i] >= '0' and items[i] <= '9') or items[i] == '$':
                flag =False
                break
                # print items[i]
            # elif items[i] == '\\' or items[i] == '(' or items[i] == '"':
            #   items
            else:
                pass
        if flag :
            items0 = items.strip()
            items1 = items0.strip('\\')
            items2 = items1.strip('(')
            items3 = items2.strip(')')
            items4 = items3.strip('"')
            items5 = items4.strip(',')
            items6 = items5.strip('.')
            items7 = items6.strip('*')
            items8 = items7.strip('\t')
            items9 = items8.strip('"')
            if items9 == '':
                pass
            else:
                new = items9
                new_wd[new] = word_dict[items]
    return new_wd

def main():
	
    # homework #2
    # 为了方便处理，我把txt的名字全部改成了
    # dt_001.txt - dt_074.txt这种比较好处理的形式
    s1 = 'data2/dt_'
    
    # 写入了排名前300的words
    writedir = 'output/data2_result.csv'
    # 写入了除去常用词的所有words
    writedir2 = 'output/data2_result2.csv'
    # 写入了所有词汇
    writedir3 = 'output/data2_result3.csv'
    App = WordReader()
    for index in range(1,74):
    	if index <= 52:
    		s2 = '.TXT'
    	else:
    		s2 = '.txt'
    	med = str(index)
    	if len(med) == 1:
    		med = '00' + med
    	elif len(med) == 2:
    		med = '0' + med
    	else:
    		pass
    	filedir = s1 + med + s2

    	all_text = read_file2(filedir)
	    # print all_text
	word_list = word_split2(all_text)

    # print word_list
    word_dict = App.word_count(word_list)
    # print word_dict
    new_wd = redu(word_dict)
    			
    # print new_wd
    key, value = App.word_sort(new_wd)
    # print word_sorted
    key1=[]
    value1=[]
    com_word =['the', 'of','to', 'a', 'in', 'and','is','that', 'on', 'it', 'was', 'from', 'has','mr',\
    'but', 'have', 'not','at', 'will', 'his','an','their','節','its','which','who','been','may','or','can','文章',\
    'if','such','most','after','like','out','when','all','says', 'over','other','this','so','what','them','no','she'\
    'might','any','than','this','since','she','might','those','just','too','before','should','i','ms','him','year',\
    '|','get']
    for index,item in enumerate(key):
    	if item not in com_word:
    		key1.append(item)
    		value1.append(value[index])
   	key2 = key1[:301]
   	value2 = value1[:301]
    App.write_csv(key2,value2,writedir)  #只取了前300词
    App.write_csv(key1,value1,writedir2) #除掉常用词
    App.write_csv(key,value,writedir3) #所有词
    # dict1 = {}
    # for i in range(1,6):
    # 	for j in range(2,7):
    # 		dict1[i] = j
    # print dict1
if __name__ == "__main__":
    main()
