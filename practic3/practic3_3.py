import turtle as tu

def traectory(Vx, Vy, ay):
    x = -300
    tu.pensize(3)
    tu.forward(300)
    tu.forward(-600)
    for j in range (1, 8, 1):
        tu.pensize(1)
        dt = 0.0
        Vx = 2 / j
        Vy = 7 - j
        y = 0
        for i in range(0, 1000, 1):
            dt += 0.0001*i
            x += Vx*dt
            y += Vy*dt + ay*dt**2/2
            Vy += ay*dt
            tu.goto(x, y)
            if y < 0:
                break

tu.shape('circle')
Vx = 1
Vy = 5
ay = -0.1
traectory(Vx, Vy, ay)

tu.exitonclick()
