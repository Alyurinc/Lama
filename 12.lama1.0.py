import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

#фон
screen.fill('grey')

#голова
circle(screen, 'yellow', (300, 300), 100)
#голова_контур
circle(screen, 0, (300, 300), 100, 1)
#глаз_левый
circle(screen, 'red', (260, 270), 20)
#глаз_левый_контур
circle(screen, 0, (260, 270), 20, 1)
#глаз_левый_зрач
circle(screen, 0, (260, 270), 9)
#глаз_левый_бровь
line(screen, 0, (200, 210), (275, 250), 10)
#глаз_правый
circle(screen, 'red', (345, 270), 15)
#глаз_правый_контур
circle(screen, 0, (345, 270), 15, 1)
#глаз_правый_зрач
circle(screen, 0, (345, 270), 8)
#глаз_правый_бровь
line(screen, 0, (330, 260), (400, 225), 10)
#рот
rect(screen, 0, (240, 340, 100, 20))

pygame.display.update()
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()