# @author: B17455
day_11:回答和解释芦苇同学提出的问题
A1:
利用遍历查询字典内容：定义了函数直接调用即可了
def print_dictionary(dictionary):
	for key in dictionary.keys():
		print '书里有%s:%s'% (key, dictionary[key])

A2: 
因为把key='abase'语句放在了search函数里面了，
所以每次调用search函数的时候，就先把变量key赋值为'abase'
在if not search('etiquetee', book, who):中变量传不进去了，
search('etiquetee', book, who)结果时False就无需执行下面语句了

