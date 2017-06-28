#!/usr/bin/python
#filename:day19practice.py

class butterfly():
	def __init__(self,name,location,action):
	   self.name=name
	   self.location=location
	   self.action=action
	def eats_an_apple(self):
		print '%s , from %s , %s ' % (self.name,self.location,self.action)

def main():
	anabela = butterfly('anabela','Portugal','eats an apple')
	anabela.eats_an_apple()
if __name__ == '__main__':
	main()
	


