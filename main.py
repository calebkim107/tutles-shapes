import turtle

turtle.title("My Cool Turtle Game")
turtle.bgcolor("grey")
turtle.setup(600, 600)
turtle.shape("turtle")

screen = turtle.Screen()
jeffery = turtle.Turtle()

input_shape = input("What shape do you want to draw?")
input_length = input("Choose how big: ")
input_color= input("Choose color:")

def triangle(length, color):
  jeffery.fillcolor(color)
  jeffery.begin_fill()

  x = 0
  while x < 3:
    jeffery.forward(int(length))
    jeffery.right(120)
    x = x+1
  jeffery.end_fill()
def square(length, color):
  jeffery.fillcolor(color)
  jeffery.begin_fill()

  x = 0
  while x < 4:
    jeffery.forward(int(length))
    jeffery.right(90)
    x = x+1
  jeffery.end_fill()
def circle(length, color):
  jeffery.fillcolor(color)
  jeffery.begin_fill()

  x = 0
  while x < 36:
    jeffery.forward(int(length))
    jeffery.right(10)
    x = x+1
  jeffery.end_fill()
def star(length, color):
  jeffery.fillcolor(color)
  jeffery.begin_fill()

  x = 0
  while x < 5:
    jeffery.forward(int(length))
    jeffery.right(144)
    x = x+1
  jeffery.end_fill()



if input_shape.lower() == "triangle":
  triangle(input_length, input_color)
elif input_shape.lower() == "square":
  square(input_length, input_color)
elif input_shape.lower() == "circle":
  circle(input_length, input_color)
elif input_shape.lower() == "star":
  star(input_length, input_color)

