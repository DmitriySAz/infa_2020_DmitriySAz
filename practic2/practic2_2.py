import turtle as tu

tu.shape('turtle')
num = 10
a = 50
for i in range(0,num,1):
    for j in range (1, 5, 1):
        tu.pendown()
        tu.forward(a+a*i)
        tu.left(90)
    tu.penup()
    tu.goto(-a/2* (i+1), -a/2* (i+1))
tu.hideturtle()
tu.exitonclick()