import turtle as tu

def draw_circle1():
    for i in range(0, 120, 1):
        tu.forward(2)
        tu.left(360 / 120)
def draw_circle2():
    for i in range(0, 120, 1):
        tu.forward(2)
        tu.right(360 / 120)

tu.shape('turtle')
tu.speed(0.5)
num = 4
for j in range (1, num):

    draw_circle1()
    draw_circle2()
    tu.left(360 / (num-1))


tu.exitonclick()