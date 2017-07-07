# -*- coding: utf-8 -*

class Dog():
  def __init__(self, name, color):
    self.name = name
    self.huahua = color

  def jump(self, hight):
    print '%s jumps %d meter' %(self.name, hight)

  def mood(self, mood):
    print 'Today %s is %s ' % (self.name, mood)

def main():

  allen = Dog('allen', 'black')
  mood = 'sad'
  allen.mood(mood)
  
  if mood == 'happy':
    allen.jump(3)
  else:
    allen.jump(1)

if __name__ == '__main__':
  main()