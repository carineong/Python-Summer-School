import math
import turtle
import random

t = turtle.Screen()
t.setworldcoordinates(-10,-10,110,110)

#if using pyln.fun online compiler please use this to view the results:
# t.setworldcoordinates(-150,-150,250,250)

t = turtle.Turtle()


# Draw circle and fill it with light gray color
t.fillcolor('light gray')
t.pencolor('light gray')
t.begin_fill()
t.penup()
t.goto(0,100)
t.pendown()
t.circle(-100,90)
t.end_fill()
t.begin_fill()
t.goto(0,100)
t.goto(0,0)
t.goto(100,0)
t.end_fill()

# Draw axis
t.pencolor("black")  
t.pensize(2)
t.penup()
t.goto(0,0)
t.pendown()
t.goto(0,100)
t.penup()
t.goto(0,0)
t.pendown()
t.goto(100,0)

# Draw dots
blue = 0
red = 0
turtle.tracer(0,0)
for i in range(10000):
  x = random.uniform(0,1)*100
  y = random.uniform(0,1)*100
  t.penup()
  t.goto(x,y)
  t.pendown()
  if(x**2+y**2)>10000:
    t.pencolor('blue')
    t.dot(2)
    blue += 1
  else:
    t.pencolor('red')
    t.dot(2)
    red += 1

# Calculate value of pi
ans = 4*(red/10000)
# print(ans)
t.penup()
t.goto(35,-5)
t.pendown()
t.pencolor('black')
t.write("π = " + str(ans),True,"consoles","5pt bold")
t.hideturtle()
turtle.update()
turtle.done()
