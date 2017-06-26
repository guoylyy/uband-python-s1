#!/usr/bin/python
# -*- coding: utf-8 -*

class Girlfriend():
  def __init__(self, name,bfname, desired_gift, favorite_color):
    self.name = name
    self.bfname=bfname
    self.desired_gift="YSL"
    self.favorite_color="13"

  def kiss(self):
    print "%s亲了%s一口"%(self.name,self.bfname)

  def argue(self):
    print "%s说：你是不是不爱我了"%(self.name)

  def gift(self, bf_gift,bf_color):
    print "情人节，%s送女朋友%s %s"%(self.bfname,self.name,bf_gift)
    if bf_gift==self.desired_gift:
      print "%s打开包装，看到色号是%s"%(self.name,bf_color)
      if bf_color==self.favorite_color:
        self.kiss()
      else:
        self.argue()
    else:
      self.argue()

def main():
  lesley=Girlfriend("lesley","xl","YSL","13")
  gift_list=["rose","ring","food","YSL"]
  color_list=['red','blue','silvery','purple','1','3','13']
  for gift in gift_list:
    for color in color_list:
      lesley.gift(gift,color)

if __name__ == '__main__':
  main()