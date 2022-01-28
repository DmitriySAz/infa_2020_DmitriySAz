import turtle as tu

tu.shape('turtle')
num = 10
a = 200
if num < 5:
    print('Невозможно построить')
elif num % 2 != 0:
    for i in range(0,num,1):
        tu.forward(-a)
        tu.left(180 - 180/num)
else:
    for i in range(0,num,1):
        tu.forward(-a)
        tu.left( - 360/num)

tu.hideturtle()
tu.exitonclick()