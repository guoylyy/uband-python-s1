#!/usr/bin/python
# -*- coding: utf-8 -*-
# 面向对象
# author:baba


class Student():
    # 属性：math, yuwen, english, physics
    # 方法：show, calSum, calAver
    
    def __init__(self, math, yuwen, english, physics):
        self.math = math + 1
        self.yuwen = yuwen
        self.english = english - 2
        self.physics = physics
        print "init: %d %d %d %d" % (self.math, self.yuwen, self.english, self.physics)
        
    def show(self):
        print "%d %d %d %d" % (self.math, self.yuwen, self.english, self.physics)
    
    def calSum(self):
        Sum = self.math + self.yuwen + self.english + self.physics
        return Sum
        
    def calAver(self):
        Sum = self.calSum()
        Aver = Sum / 4
        return Aver

def main():
    xiaoming = Student(99, 89, 110, 100)
    xiaoming.show()
    print "%d" % xiaoming.calAver()
    
    

if __name__ == '__main__':
    main()
    