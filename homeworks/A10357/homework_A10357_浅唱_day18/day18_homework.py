#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

class Pineapple():
    def __init__(self, usage1, usage2):
        self.usage1 = usage1
        self.usage2 = usage2
    def what_use(self):
        print '菠萝不仅可以%s ，而且可以%s' % (self.usage1, self.usage2)

def main():
    pp = Pineapple('eat','plant')
    pp.what_use()

if __name__ == '__main__':
  main()
