import turtle as tu
import math

def draw_squad(n, b):
    n = 2+n
    tu.left(180 - (180 - 360 / n)/2)
    for i in range(1,n+1, 1):
        tu.forward(b)
        tu.left(360 / n)
    tu.right(180 - (180 - 360 / n)/2)


tu.shape('turtle')
num = 11
step = 20
r = 20
for j in range (1, num):
    a = r*2*abs(math.sin(math.pi/180*180/(j+2)))
    draw_squad(j, a)
    r += step
    tu.penup()
    tu.forward(step)
    tu.pendown()

tu.exitonclick()