import turtle as tu

def draw_circle1(x):
    for i in range(0, 120, 1):
        tu.forward(2+x)
        tu.left(360 / 120)
def draw_circle2(x):
    for i in range(0, 120, 1):
        tu.forward(2+x)
        tu.right(360 / 120)

tu.shape('turtle')
tu.speed(0.5)
tu.left(90)
num = 4
for j in range (1, num):

    draw_circle1(j)
    draw_circle2(j)
#    tu.left(360 / (num-1))


tu.exitonclick()