import pygame
from pygame.draw import *

def create_display(A):
    '''Function which create display for drawing figures'''
    screen = pygame.display.set_mode(A, 0, 0, 0, 0)
    return screen

def draw_Paint(x, y, screen):
    """Draw the Painting"""
    screen.fill(rosybrown)
    rect(screen, salmon, (0, 0, 1500, 250))
    rect(screen, LightSalmon, (0, 250, 1500, 200))
    rect(screen, SandyBrown, (0, 450, 1500, 200))
    circle(screen, yellow, (x, y), 100)
    polygon(screen, OrangeRed, [(0, 480), (1500, 400), (1400, 360), (1350, 390), (1150, 50), (1050, 200),
                                (950, 150), (850, 400), (0, 300)])
    z = 0
    y1 = 0
    y2 = 1080
    for i in range(1, 50, 1):
        line (screen, black, (z, y1), (z, y2))
        z+=50



# Используемые в проге цвета
OrangeRed = (255, 69, 0)
rosybrown = (188, 143, 143)
salmon = (250, 128, 114)
LightSalmon = (255, 160, 122)
SandyBrown = (244, 164, 96)
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

disp_size = (1500, 780) #Размер экрана, от него зависит размер смайла

pygame.init()
screen = create_display(disp_size)
draw_Paint(disp_size[0]//2, disp_size[1]//4, screen)
pygame.display.update()
clock = pygame.time.Clock()
finished = True
FPS = 30
while finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = False

pygame.quit()
