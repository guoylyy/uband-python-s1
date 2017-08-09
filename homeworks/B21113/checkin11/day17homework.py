import turtle
def main():
    t = turtle.Turtle()
    t.hideturtle()
    lengthOfSize = 200
    drawFivePointStar(t,0,0,lengthOfSize)
def drawFivePointStar(t,x,y,lengthOfSize):
    t.up()
    t.goto(x,y)
    t.left(36)
    t.down()
    for i in range(5):
        t.forward(lengthOfSize)
        t.left(144)
main()