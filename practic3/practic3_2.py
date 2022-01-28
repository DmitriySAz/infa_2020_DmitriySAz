from random import *
import turtle as t

def draw_0(x):
    t.color('blue')
    t.right(90)
    t.forward(2*x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(2*x)
    t.right(90)
    t.backward(x)
    t.forward(x)

def draw_1(x):
    t.color('blue')
    t.penup()
    t.right(90)
    t.forward(x)
    t.left(90+45)
    t.pendown()
    t.forward(2**0.5 * x)
    t.right(90 + 45)
    t.forward(2*x)
    t.forward(-2 * x)
    t.left(90)

def draw_2(x):
    t.color('blue')
    t.forward(x)
    t.right(90)
    t.forward(x)
    t.right(45)
    t.forward(2**0.5 * x)
    t.left(90+45)
    t.forward(x)
    t.penup()
    t.left(90)
    t.forward(2*x)
    t.right(90)

b = 30
t.speed()
A = []



