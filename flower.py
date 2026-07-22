import turtle


window = turtle.Screen()
window.bgcolor("black")


flower = turtle.Turtle()
flower.speed(0)  


colors = ["red", "purple", "blue", "green", "yellow", "orange"]


for x in range(150):
    flower.pencolor(colors[x % 6]) 
    flower.width(x / 100 + 1)       
    flower.forward(x)              
    flower.left(59)                 


turtle.done()
