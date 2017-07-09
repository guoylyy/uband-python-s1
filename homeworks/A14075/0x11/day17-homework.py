import turtle
import time
def main():
    win = turtle.Screen()
    ty = turtle.Turtle()
    ty.shape('arrow')
    ty.color('blue')
    ty.begin_fill()
    ty.circle(80)
    ty.end_fill()
    ty.color("red")
    ty.goto(100,120)
    ty.write("Hello,world!",True,align="center")
    time.sleep(3)
if __name__ == "__main__":
    main()
