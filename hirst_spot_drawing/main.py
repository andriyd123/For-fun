""" import colorgram 

colors = colorgram.extract('spot_painting.jpeg', 20)


color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))
print(color_list)  """

import turtle as t
import random

t.colormode(255)
jim = t.Turtle()
jim.speed("fastest")
jim.penup()
jim.hideturtle()
color_list = [(209, 165, 124), (140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (171, 186, 177), (27, 197, 220), (232, 165, 190), (189, 49, 36), (118, 48, 131), (72, 149, 239), (255, 140, 0)]

jim.setheading(225)
jim.forward(300)
jim.setheading(0)

number_of_dots = 100

for i in range(1, number_of_dots + 1):
    jim.dot(20, random.choice(color_list))
    jim.forward(50)

    if i % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)

Screen = t.Screen()
Screen.exitonclick()