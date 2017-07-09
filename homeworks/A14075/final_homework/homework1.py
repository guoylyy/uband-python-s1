# -*- coding: utf-8 -*-
import os
import codecs 

#扫描目录中文件 返回文件列表
def get_file_from_folder(folder_path):
    file_paths = []
    #root-当前目录位置 dirs-当前目录中目录 files-当前文件 
    for root,dirs,files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root,file) #位置-文件名
            file_paths.append(file_path)
    print ("扫描到%d个文件"%(len(file_paths)))
    return file_paths

#打开当前文件 返回由各行组成的列表
def format_line(line):
    fmt = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #print(line)
    for char in line:
        flag = char in fmt
        if (not flag):            
            line = line.replace(char,' ')  #用空格替换非字符
    #print(line.lower())
    return line.lower()

def file_process(file_path):
    words = []
    f = codecs.open(file_path, 'r' ,'utf-8')
    lines = f.readlines() #按行返回列表
    for line in lines:
        line = line.strip() #删除\n
        newline = format_line(line) #格式化
        wordline = newline.split(' ') #分隔
        words.extend(wordline)
    #print (len(words),words)
    
    return words

def read_files(file_paths):
    words = []
    for index,file_path in enumerate(file_paths):
        wordfile = file_process(file_path)
        words.extend(wordfile)
        if (index+1)%10==0:
            print ("已处理%d个文件"%(index+1))
    print("处理完成")
    return words

def generDict(words):
    dic = {}
    for word in words:
        #删除空白和单字母
        if len(word)>1:
            if word in dic:
                dic[word]+=1
            else :
                dic[word] = 1
    return dic            

def print_to_csv (dic,to_file_path):
    nfile = codecs.open(to_file_path , "w+")
    for key in dic.keys():
        val = dic[key]
        nfile.write("%s,%s\n"%(key,str(val)))
    nfile.close()
    print ("已输出词频")

def main(): 
    folder_path = '.\\data2'        #should modify
    to_file_path = ".\\output\\test.csv"
    file_paths = get_file_from_folder(folder_path)
    words = read_files(file_paths)
    wordDict = generDict(words)
    print_to_csv(wordDict,to_file_path)
    
if __name__ == "__main__":
    main()
