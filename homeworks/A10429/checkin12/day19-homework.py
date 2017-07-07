#!/usr/bin/python
# -*- coding: utf-8 -*-
class cell():
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def migration(self):
		print '一株来自%s ，名字叫做%s 的细胞迁移了 ' %(self.location, self.name)

def main():
  hela = cell('hela', 'USA')
  hela.migration()

if __name__ == '__main__':
  main()