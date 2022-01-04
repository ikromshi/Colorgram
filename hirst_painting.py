import turtle as t
import random
tim = t.Turtle()
t.colormode(255)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")
dots = 100
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227),
 (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36),
 (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151)]

for dot_num in range(1, dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_num % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
