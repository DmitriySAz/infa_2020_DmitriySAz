from random import *
import turtle as t


t.speed(20)
for i in range (1, 200):
    n = random()
    t.left(n*360)
    t.forward(30*n)
    print(round(n*360, 2))
