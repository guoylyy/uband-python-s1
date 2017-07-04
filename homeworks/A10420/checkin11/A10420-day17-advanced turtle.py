import turtle 

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()

# painter = turtle.Turtle()

# painter.pencolor("blue")

# for i in range(50):
#     painter.forward(50)
#     painter.left(123) # Let's go counterclockwise this time 
    
# painter.pencolor("red")
# for i in range(50):
#     painter.forward(100)
#     painter.left(123)
    
# turtle.done()