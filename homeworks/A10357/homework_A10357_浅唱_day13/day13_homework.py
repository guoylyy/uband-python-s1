#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

def main():
    week_outside = [False, False, True, False, False]
    for index,is_outside in enumerate (week_outside):
        print "今天是星期%d" % (index + 1)
        
        try:
            check(is_outside)
        except Exception,e:
            print '%s' % (e)
            
def check(is_outside):
    if is_outside:
        raise Exception('老妈把老爸打了一顿，原谅了他')       
    else:
        print '今日相安无事'
    







if __name__ == '__main__':
  main()