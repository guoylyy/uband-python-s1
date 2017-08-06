#!/usr/bin/python
# -*- coding: utf-8 -*

class Player():
	def __init__(self, name, position):
		self.name=name
		self.position=position
		self.pts=0
	
	def two_pt(self):
		print '%s knocks it down!'%(self.name)
		self.pts=self.pts+2

	def three_pt(self):
		print '%s from downtown! Got it!'%(self.name)
		self.pts=self.pts+3

	def show_pts(self):
		print '%s has got %d points.'%(self.name, self.pts)

	def show_pos(self):
		print '%s plays %s.'%(self.name, self.position)

def main():
	LeBron=Player('LeBron', 'SF')
	LeBron.show_pos()
	LeBron.two_pt()
	LeBron.two_pt()
	LeBron.three_pt()
	LeBron.three_pt()
	LeBron.show_pts()

if __name__=='__main__':
  main()