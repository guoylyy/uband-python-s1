#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

def main():
	study_hardly=[True,True,True,False,True,True,False]#一周的学习情况
	for index, is_study in enumerate(study_hardly):
		print '今天星期%d '%(index+1)
		print is_study#学习情况

		try:
			study_cheak(is_study)	
		except Exception,e:
			#发生错误的情况
			print '发生了错误：%s '%(e)	
			print '挨了一顿打，然后继续学习 '
		else:
			#没有错误的情况
			print '学习成绩提高 '	
		print '--------------'	

#奖励和惩处判断程序
#好好学习给予奖励，反之处罚
def study_cheak(is_study)	:
	if is_study:
		print '美食奖励 '
	else:
		raise Exception('挨打 ')#发生错误中断程序	

if __name__ =='__main__':
	main()