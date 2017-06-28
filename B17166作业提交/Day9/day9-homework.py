#!/usr/bin/python
#filename:day9-homework.py

def main():
	dictionary = {'good':'of a favorable character or tendency','none':'not any such thing or person','nice':'very beautiful'}
	print len(dictionary)
	print dictionary.keys()
	print dictionary.values()

	print dictionary.has_key('good')
	
	print dictionary.has_key('bad')

	dictionary['bad']='failing to reach an accepatable standard'
	print dictionary

	del dictionary['bad']
	print dictionary
	print len(dictionary)


	print '-----'
	print dictionary['good']
	if dictionary.has_key('bad'):
		print dictionary['bad']
	else:
		print 'there is no bad'

	for key in dictionary.keys():
		print key
		print dictionary[key]
if __name__ == '__main__':
	main()





