class Man():
	def __init__(self, name, look, edu):
		self.name = name 
		self.look = look
		self.edu = edu

	def intro(self):
		print "The %s guy is called %s" % (self.look, self.name)
	def education(self):
		print "%s has a %s degree" % (self.name, self.edu)	
	def dump(self):
		print "%s is going to dump you" % (self.name)


def main():
	Zhou = Man('Zhou', 'handsome', 'Master')
	Zhou.intro()
	Zhou.education()
	Zhou.dump()
	
if __name__ == '__main__':
  main()