import turtle as tu

tu.shape('turtle')
num = int(input('Enter number of angles'))
for i in range(1,num+1,1):
    tu.forward(5)
    tu.left(360 / num)
tu.exitonclick()


