# -*- coding: utf-8 -*-


import codecs
import os

#读取文件
#会出现有些单词全用连字符号连在了一起
#['aa','aaa-a-vv']  >>>> ['aa', 'aaa', 'a', 'vv']
def word_split(words):
    new_list = []
    for word in words:
        if '-' not in word:
            new_list.append(word)
        else:
            lst = word.split('-')
            new_list.extend(lst)
    return new_list


#1读取文本
def read_file(file_path):
    f = codecs.open(file_path, 'r', "utf-8")   #打开文件读取
    lines = f.readlines()    #一行行的读单词
    word_list = []
    for line in lines:
        line = line.strip()  #把左右空格都去掉
        words = line.split(" ")       #用空格分割 
        words = word_split(words) #用-分割
        word_list.extend(words)   #在列表末尾一次增加另一个列表的多个值
    return word_list

#读取多个文件
def read_files(file_paths):
    final_words = []
    for path in file_paths:
        final_words.extend(read_file(path))
    return final_words

def get_file_from_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths

#2.获取格式化之后的单词
def format_word(word):
    fmt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'
    for char in word:
        if char not in fmt:
            word = word.replace(char, '')
    return word.lower()

def format_words(words):    #搞个函数让这个格式针对全部的单词
    word_list = []
    for word in words:    #也就是整个循环跑一次 用for
        wd = format_word(word)
        if wd:
            word_list.append(format_word(word))    #在词尾添加新对象
    return word_list



#3 统计单词数目      用字典  可以方便查找  
# {'aa': 1} 如果字典里有aa的话，就是1了。那下次再查，有的话就把数值变成2
def statictcs_word(words):
    s_word_dic = {}
    for word in words:
        if s_word_dic.has_key(word):
            s_word_dic[word] = s_word_dic[word] + 1    #值加1
        else:
            s_word_dic[word] = 1
    return s_word_dic


#4.输出成csv
def print_to_csv(volcaulay_map, to_file_path):
    nfile = open(to_file_path,'w+')
    for key in volcaulay_map.keys():
        val = volcaulay_map[key]
        nfile.write("%s,%s\n" % (key, str(val)))
    nfile.close()


def main():

    #读取文本
    # paths = get_file_from_folder('data2')
    words = read_files(get_file_from_folder('data2'))   
    # words = read_file('data1/dt01.txt')    #读取单个文件的时候
    # print words
    print '获取了未格式化的单词 %d 个' % (len(words))

    #整理文本
    # print format_word('Aaa 8223')   #但是这样是针对单个单词的
    f_words = format_words(words)
    # print f_words
    print '获取了一格式化的单词 %d 个' % (len(f_words))

    # 统计单词
    word_dict = statictcs_word(f_words)

    #输出单词
    print_to_csv(word_dict, 'output/test.csv')

if __name__ == '__main__':
    main()