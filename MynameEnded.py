import turtle
def draw_myname():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.speed(3)
    brad.color("red")
    brad.right(180)
    brad.forward(200)
    brad.right(180)
    draw_A(brad)
    draw_D(brad)
    draw_R(brad)
    draw_I(brad)
    draw_E(brad)
    draw_N(brad)


def draw_A(line):
    line.color("white")
    line.left(90)
    line.forward(100)
    line.right(90)
    line.forward(50)
    line.right(90)
    line.forward(50)
    line.right(90)
    line.forward(50)
    line.right(180)
    line.forward(50)
    line.right(90)
    line.forward(50)
    line.left(90)
    line.color("red")
    line.forward(25)
    
def draw_D(line):
    line.color("white")
    line.left(90)
    line.forward(100)
    line.right(135)
    line.forward(70.71)
    line.right(90)
    line.forward(70.71)
    line.left(135)
    line.color("red")
    line.forward(75)
    

def draw_R(line):
    line.color("white")
    line.left(90)
    line.forward(100)
    line.right(90)
    line.forward(25)
    line.right(45)
    line.forward(35.3)
    line.right(90)
    line.forward(35.3)
    line.right(45)
    line.forward(25)
    line.left(135)
    line.forward(70.71)
    line.left(45)
    line.color("red")
    line.forward(25)


def draw_I(line):
    line.color("white")
    line.forward(50)
    line.right(180)
    line.forward(25)
    line.right(90)
    line.forward(100)
    line.left(90)
    line.forward(25)
    line.right(180)
    line.forward(50)
    line.color("red")
    line.forward(25)

def draw_E(line):
    line.color("white")
    line.forward(50)
    line.right(180)
    line.forward(50)
    line.left(90)
    line.forward(50)
    line.left(90)
    line.forward(25)
    line.right(180)
    line.forward(25)
    line.left(90)
    line.forward(50)
    line.left(90)
    line.forward(50)
    line.color("red")
    line.forward(25)

def draw_N(line):
    line.color("white")
    line.left(90)
    line.forward(100)
    line.right(150)
    line.forward(111)
    line.left(150)
    line.forward(100)
    
draw_myname()


    
    


    
