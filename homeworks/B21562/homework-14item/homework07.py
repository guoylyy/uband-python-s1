#-*- coding:utf-8 -*-

#定义一个字典

def dictionary():
	dic={"书":"book","笔":"pen","纸":"paper"}
	dic2={'1+2':3,
			'2+3':5,
			'5*6':30,
			'7-3':4,
			'8/4':2
			} #字典里的词条可以写在一排，也可以换行，但一定要记得用逗号隔开
	dic3={'list1':[1,3,5,7,9],9:[8,7,6,5,4,3,2,1]} #字典的值也可以是一个列表
	dic5={'1':{'1+2':3,'3+5':8},'2':{'1*2':2,"3*5":15}} #字典的值还可以是一个字典
	return dic,dic2,dic3,dic5
def print2(dic2):
	for i in dic2.keys(): #遍历dic2中的每一个键
		if dic2[i]%2==0:
			print i
		else:
			print '%s=%d'%(i,dic2[i])
def print3(dic):
	for n in dic.values():  #遍历dic中的每一个值
		print n
def print5(dic):
	dic["爱"]='love' #在字典中加入一个新的键
	dic['书']='books' #替换一个已经存在的键值
	del dic['爱'] #删除一个键值
	dic.clear() #清空字典里所有的值
	print dic.values()

def main():
	dic,dic2,dic3,dic5=dictionary()
	print len(dic) #字典的长度，即字典中有多少个key（value）
	print len(dic2)
	print dic2.keys() #获得一个列表，列举出字典里的key，注意不是按字典里写的顺序列举的
	print dic.values() #获得一个列表，列举出字典里所有的值
	print dic3['list1'][1] #当字典里的值是一个列表时，可以print列表中的某一项
	print dic5['1']['3+5'] #当字典里的值是字典时，可以获得字典中某个key的某项取值
	print dic.has_key("书") #当字典里存在某个key值时，返回True
	print dic2.has_key(1) #当字典里不存在这个key值时，返回false
	print2(dic2)
	print3(dic)
	print5(dic)

if __name__ == '__main__':
	main()