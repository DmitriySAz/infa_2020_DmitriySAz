import turtle as tu

def draw_circle1(x):
    for i in range(0, 45, 1):
        tu.forward(x)
        tu.right(360 / 90)
def draw_circle2(x):
    for i in range(0, 45, 1):
        tu.forward(x)
        tu.right(360 / 90)

tu.shape('turtle')
tu.speed(10)
tu.left(90)
num = 10
tu.penup()
tu.goto(-300, 0)
tu.pendown()
for j in range (0, num):
    draw_circle1(3)
    if j < num-1:
        draw_circle2(3/4)

tu.exitonclick()