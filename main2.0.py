import pygame
import math
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 800))
# фон
rect(screen, (175, 221, 233), (0, 0, 700, 350))
rect(screen, (170, 222, 135), (0, 350, 700, 700))

#цветы
def flower(x, y, size, angle):
    surf = pygame.Surface((100, 100), pygame.SRCALPHA)
    ellipse(surf, (255, 255, 255), (15 * size, 20 * size, 9 * size, 19 * size))
    arc(surf, (149, 162, 139), (15 * size, 20 * size, 10 * size, 20 * size), 0, 2 * math.pi)
    ellipse(surf, (255, 255, 255), (10 * size, 10 * size, 9 * size, 20 * size))
    arc(surf, (149, 162, 139), (10 * size, 10 * size, 9 * size, 20 * size), 0, 2 * math.pi)
    ellipse(surf, (255, 255, 255), (10 * size, 30 * size, 9 * size, 20 * size))
    arc(surf, (149, 162, 139), (10 * size, 30 * size, 10 * size, 20 * size), 0, 2 * math.pi)
    ellipse(surf, (255, 255, 0), (7 * size, 20 * size, 10 * size, 20 * size))
    ellipse(surf, (255, 255, 255), (3 * size, 10 * size, 9 * size, 20 * size))
    arc(surf, (149, 162, 139), (3 * size, 10 * size, 10 * size, 20 * size), 0, 2 * math.pi)
    ellipse(surf, (255, 255, 255), (3 * size, 30 * size, 9 * size, 20 * size))
    arc(surf, (149, 162, 139), (3 * size, 30 * size, 10 * size, 20 * size), 0, 2 * math.pi)
    ellipse(surf, (255, 255, 255), (0 * size, 20 * size, 10 * size, 20 * size))
    arc(surf, (149, 162, 139), (0 * size, 20 * size, 10 * size, 20 * size), 0, 2 * math.pi)
    surf = rotate(surf, angle)
    screen.blit(surf, (100 + x, 100 + y))

def klumb(x, y, size):
    circle(screen, (113, 200, 55), (400 * size + x, 670 * size + y), 80 * size)
    flower(260 * size + x, 430 * size + y, 1 * size, 90)
    flower(190 * size + x, 430 * size + y, 0.8 * size, 120)
    flower(300 * size + x, 450 * size + y, 1.2 * size, 60)
    flower(230 * size + x, 480 * size + y, 1 * size, 100)
    flower(320 * size + x, 520 * size + y, 1 * size, 30)
    flower(260 * size + x, 525 * size + y, 1.2 * size, 80)
#горы
polygon(screen, (179, 179, 179), [(800, 470), (400, 470), (380, 460), (380, 420), (375, 415),
                                  (375, 400), (370, 390), (370, 394), (200, 390), (150, 395),
                                  (120, 390), (50, 395), (-100, 405), (50, 100), (100, 200),
                                  (170, 120), (350, 300), (400, 100), (440, 150), (500, 20)])
aalines(screen, (0, 0, 0), True, [(800, 470), (400, 470), (380, 460), (380, 420), (375, 415),
                                  (375, 400), (370, 390), (370, 394), (200, 390), (150, 395),
                                  (120, 390), (50, 395), (-100, 405), (50, 100), (100, 200),
                                  (170, 120), (350, 300), (400, 100), (440, 150), (500, 20)], 1000)

#лама
# !!! size>0 !!!!!
def lama(x, y, size):
    polygon(screen, (255, 255, 255), [(200 * size + x, 270 * size + y), (180 * size + x, 240 * size + y),
                                      (182 * size + x, 245 * size + y), (200 * size + x, 260 * size + y),
                                      (220 * size + x, 265 * size + y)])
    aalines(screen, (255, 255, 255), True, [(200 * size + x, 270 * size + y), (180 * size + x, 240 * size + y),
                                      (182 * size + x, 245 * size + y), (200 * size + x, 260 * size + y),
                                      (220 * size + x, 265 * size + y)], 1000)

    polygon(screen, (255, 255, 255), [(217 * size + x, 265 * size + y), (197 * size + x, 235 * size + y),
                                      (199 * size + x, 240 * size + y), (217 * size + x, 255 * size + y),
                                      (237 * size + x, 260 * size + y)])
    aalines(screen, (255, 255, 255), True, [(217 * size + x, 265 * size + y), (197 * size + x, 235 * size + y),
                                      (199 * size + x, 240 * size + y), (217 * size + x, 255 * size + y),
                                      (237 * size + x, 260 * size + y)], 1000)

    surf1 = pygame.Surface((500, 500), pygame.SRCALPHA)
    surf2 = pygame.Surface((100, 100), pygame.SRCALPHA)
    ellipse(surf1, (255, 255, 255), (200, 200, 40, 70))

    ellipse(screen, (255, 255, 255), (200 * size + x, 285 * size + y, 50 * size, 150 * size))

    ellipse(surf1, (255, 255, 255), (30, 80, 70, 170))

    ellipse(screen, (255, 255, 255), (90 * size + x, 415 * size + y, 25 * size, 65 * size))
    ellipse(screen, (255, 255, 255), (90 * size + x, 475 * size + y, 28 * size, 60 * size))
    ellipse(screen, (255, 255, 255), (98 * size + x, 532 * size + y, 30 * size, 20 * size))

    ellipse(screen, (255, 255, 255), (185 * size + x, 410 * size + y, 25 * size, 70 * size))
    ellipse(screen, (255, 255, 255), (185 * size + x, 475 * size + y, 28 * size, 60 * size))
    ellipse(screen, (255, 255, 255), (193 * size + x, 532 * size + y, 30 * size, 20 * size))

    ellipse(screen, (255, 255, 255), (130 * size + x, 440 * size + y, 25 * size, 70 * size))
    ellipse(screen, (255, 255, 255), (130 * size + x, 505 * size + y, 28 * size, 60 * size))
    ellipse(screen, (255, 255, 255), (138 * size + x, 562 * size + y, 30 * size, 20 * size))

    ellipse(screen, (255, 255, 255), (210 * size + x, 440 * size + y, 25 * size, 70 * size))
    ellipse(screen, (255, 255, 255), (210 * size + x, 505 * size + y, 28 * size, 60 * size))
    ellipse(screen, (255, 255, 255), (218 * size + x, 562 * size + y, 30 * size, 20 * size))

    surf1 = rotate(surf1, 90)
    screen.blit(surf1, (0 + x, 0 + y))

    circle(screen, (229, 128, 255), (230 + x, 275 + y), 13 * size)
    circle(screen, (0, 0, 0), (235 + x, 273 + y), 6 * size)

    ellipse(surf2, (255, 255, 255), (0, 0, 6, 14))
    surf2 = rotate(surf2, 65)
    screen.blit(surf2, (222 + x, 177 + y))

lama(-50, 100, 1)
lama(200, 0, 1)
klumb(0, 0, 1,)
klumb(-150, -200, 1)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()