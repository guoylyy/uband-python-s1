# -*- coding: UTF-8 -*-  
#author fangcheng

#1.list
def main():
	dictionary = {
                 'good':'of a favoriable character or tendenc',
                 'none':'not any such thing or person',
                 'dsada':'wsd sdf dsf dsgftr54 sdw',
                 'ghf':'fgsdf dsf h ewrw tfw'
	             }
	for key in dictionary:
		print key ,'correspond to ',dictionary[key]
	#字典长度
	print len(dictionary)
	#获得key值
	print dictionary.keys()
	#获得value值
	print dictionary.values()
	#判断某个值是否存在于字典中
	print dictionary.has_key('good')
	print dictionary.has_key('good2')
	#add 添加
	dictionary['bad'] = 'fdefw'
	print dictionary
	#modify 修改
	dictionary['bad'] = 'suchsd'
	print dictionary
	#delete 删除
	del dictionary['bad']
	print dictionary
	#for 循环
	for key in dictionary.keys():
		print dictionary[key]

if __name__ == '__main__':
	main()