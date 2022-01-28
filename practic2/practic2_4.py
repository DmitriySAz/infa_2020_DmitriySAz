import turtle as tu

tu.shape('turtle')
num = 10
f = 360
a = 30
for i in range(0, 30, 1):
    tu.forward(a+a/2*i)
    tu.left(90)

tu.hideturtle()
tu.exitonclick()