#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象

def main1():
  distance = 20

  e_bicycle = '电动车'
  bicycle = '自行车'

  day1 = '周一'
  hour1 = 0.5
  speed1 = 20/hour1
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

  day2 = '周二'
  hour2 = 2
  speed2 = 20/hour2
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

  day3 = '周三'
  hour3 = 0.6
  speed3 = 20/hour3
  

#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度


#分析最后要输出什么话，print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)  → 第二次输入 → 第二次输入要用的变量
# 需要引入day,  self.name,  speed(20/hour)  

#第一次初始值就要引入self,name

# →   day , self, hour  +前面计算公式  
# 调序（self最前）→self,day,hour




#以下略过
#（ 2个工具：e_bicycle  bicycle  → Bicycle(name)
#  distance=20
#  hour 
# 漏了1个：day

# 求speed=20/hour（倒推回去，引入hour的变量）

# main函数就要有3个变量
# 本身：bicycle(name) hour 初始值      后来发现本身self和变量并没有绝对关联，hour也可以第二次直接引入，不用说一定要用self.hour的格式
# 第二次引入distance+计算            后来也发现不一定

#重点是class里的函数能和main函数相对应即可）

class Bicycle():
  
  def __init__(self, day,name, hour):   #有个问题：其实day不属于车本身的东西，并不应该被定义进初始值
    self.day = day 
    self.name  = name
    self.hour  = hour

  def ride(self):
    speed=20/self.hour
    print '老妈星期%s 骑 %s 平均时速 %0.2f km/h' %(self.day,self.name, speed)

def main2():
  e_bicycle=Bicycle(1,'e_bicycle',0.5)
  e_bicycle.ride()

  bicycle=Bicycle(2,'bicycle',2)
  bicycle.ride()

  e_bicycle=Bicycle(3,'e_bicycle',0.6)
  e_bicycle.ride() 





class Bicycle():
  
  def __init__(self, name):
    
    self.name  = name #或者也可以在这里定义self.hour=hour,下面就不用再引入hour,只需代值hour
 

  def ride(self,day,hour):   #上面有的就不用继续定义   可以这里直接开始设置新的变量day和hour

    speed=20/hour     #之前的作业是self.speed，但这里并不用。也就是说，不是说speed就要加self。 
                       #变量跟self有无关系并不重要，重要的是从print的内容入手引入变量


    print '老妈星期%s 骑 %s 平均时速 %0.2f km/h' %(day,self.name, speed)


def main3():
  e_bicycle=Bicycle('电动车')  #原来写成e_bicycle,实际上应写成电动车
  e_bicycle.ride(1,0.5)    #主要是在这里对应输入day和hour的数值

  bicycle=Bicycle('自行车')
  bicycle.ride(2,2)

  e_bicycle=Bicycle('电动车')
  e_bicycle.ride(3,0.6)  





if __name__ == '__main__':
  main3()


# 总结：
# 思维误区：
# 1.不相关的变量day,hour都把它和self联系在一起   但实际上跟车本身并无关，它只是一个纯粹的变量

# 2.之前的思路是先找出跟self有关的变量，然后其他的变量第二次再引入
#   但实际上只有name是确定在self里面的，其他的无法确定
#   eg.无法确定speed和hour是否一定是车本身self的内容，是否一定要写在ini里面
#   事实证明不是，sample code里面是self.speed,但在这里是speed

#   ∴重要的是从问题，从要print的内容入手，寻找需要引入的变量

# 金句：
#    print的内容→第二次要输出的结果→找第二次要输出的变量