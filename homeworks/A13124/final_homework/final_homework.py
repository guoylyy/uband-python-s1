

import codecs
import os
#1.读入数据
def read_file(file_path):
	f = codecs.open('file_path','r','utf-8')
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		words = line.split(' ')
		print words
    return words
#2.格式化数据

#3.输出数据

#4.统计数据
def main():
	# read_file('date1/dt01.txt')
	print 'aa'
if __name__ == '__main__':
	main()
