#!/usr/bin/python
#-*- coding:utf-8 -*-
# a={' q':7,' op':2,' ui':5}
# items = a.items()
# print items
# items.sort()
# print items
# sorted1 = sorted(a.items(),key=lambda a:a[1])
# sorted1.reverse()
# print len(sorted1)
# print '----'
# b={}
# # del a['q']
# for item in a.keys():
# 	new = item.strip()
# 	b[new] = a[item]
# print a
# print b
# c = '"op'
# print c
# print c.strip('"')
# print c
# d = ' 3d 6rt \tyu'
# print d
# print d.strip()
com_word =['one']
f = ['er','one','ti']
print f
for i in range(0,len(f)):
    	if f[i] in com_word:
    		print f[i]
    		del f[i]
    		# del value[i]
print f