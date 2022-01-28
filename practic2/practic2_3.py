import turtle as tu

tu.shape('turtle')
num = 12
a = 100
for i in range(0,num,1):
    tu.right(360 / num)
    tu.forward(a)
    tu.stamp()
    tu.left(180)
    tu.forward(a)
    tu.left(180)

tu.hideturtle()
tu.exitonclick()