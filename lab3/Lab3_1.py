import pygame
from pygame.draw import *

def create_display(A):
    '''Function which create display for drawing figures'''
    screen = pygame.display.set_mode(A, 0, 0, 0, 0)
    return screen

def draw_smile(x, y, screen):
    """Draw angry smile in display"""
    screen.fill(white)
    circle(screen, yellow, (x, y), x/2)
    circle(screen, red, (x-x/5, y*4/5), x/10)
    circle(screen, black, (x-x/5, y*4/5), x/20)
    circle(screen, red, (x+x/5, y*4/5), 0.075*x)
    circle(screen, black, (x+x/5, y*4/5), x/22)
    line(screen, black, (x-x/5, y*5/4), (x+x/5, y*5/4), x//15)
    line(screen, black, (x - x / 25, y * 3.5 / 5), (0.5 * x, 0.5 * y), x // 20)
    line(screen, black, (x + x / 25, y * 3.8/ 5), (1.5 * x, 0.5 * y), x // 20)


# Используемые в проге цвета
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

disp_size = (1000, 700) #Размер экрана, от него зависит размер смайла

pygame.init()
screen = create_display(disp_size)
draw_smile(disp_size[0]//2, disp_size[1]//2, screen)
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
