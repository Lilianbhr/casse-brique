import pygame
from classes import *
pygame.init()

# Fenêtre
gap = 50
largeur = 2 * gap + 800
hauteur = gap + 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Casse Brique")
bg = pygame.Color(20, 20, 20)

paddle = Paddle()

clock = pygame.time.Clock()
running = True
while running :
    screen.fill(bg)
    paddle.update()
    total.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                paddle.direction = 1
                break
            elif event.key == pygame.K_LEFT :
                paddle.direction = -1
                break
        elif event.type == pygame.KEYUP :
            paddle.direction = 0
    pygame.display.flip()
    clock.tick(60)

pygame.quit()