#!usr/bin/python
#coding:utf-8

class tools():
	"""docstring for speed"""
	distance = 20
	def __init__(self,tool):
		self.tool = tool
	def speed(self,day,hour):
		sp = tools.distance/hour
		print '%s 骑 %s 平均时速 %0.2f km/h' %(day,self.tool, sp)
		

def main():
	tool1 = tools("电动车")
	tool2 = tools("自行车")
	tool1.speed("周一",0.5)
	tool2.speed("周二",2)
	tool1.speed("周三",0.6)



if __name__ == '__main__':
	main()