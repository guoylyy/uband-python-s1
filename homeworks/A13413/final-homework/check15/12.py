# -*- coding: utf-8 -*-

import codecs
import os

def read_file(file_path):
	f = codecs.open(file_path, 'r', "utf-8")
	lines = f.readlines()

	for line in lines:
		line = line.strip()
		words = line.split(' ')
		print words
	return words
def main():
	read_file('data1/dt01.txt')
if __name__ == '__main__':
	main()
