# -*- coding: utf-8 -*-
# @author: shuan

print '1'

import time
import calendar

def main():
    ticks=time.time()
    print '现在的时间是：', ticks

    localtime = time.localtime(time.time())
    print '当地时间为：',localtime

    asctime = time.asctime(time.localtime(time.time()))
    print '时间为：', asctime
    
    strftime1= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print "现在是：", strftime1

    strftime2= time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
    print "        ",strftime2

    strftime3= time.mktime(time.strptime(strftime2))
    print '时间戳转换：', strftime3

    cal= calendar.month(2017,1)
    print '一月日历'
    print cal


if __name__ == '__main__':
 main()