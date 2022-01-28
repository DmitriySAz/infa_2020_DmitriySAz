from random import randint
import turtle as tu


number_of_turtles = 100
steps_of_time_number = 200

pool = [tu.Turtle(shape='circle') for i in range(number_of_turtles)]
for un in pool:
    un.penup()
    un.speed(50)
    un.goto(randint(-200, 200), randint(-200, 200))
    un.seth(randint(0, 360))
    #un.seth(300)

for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(5)
        x = unit.pos()[0]
        y = unit.pos()[1]
        #print(unit.heading())
        if abs(x) >= 200:
            unit.seth(180-unit.heading())
        if abs(y) >= 200:
            unit.seth(360-unit.heading())
        #print(x, y)

tu.exitonclick()
