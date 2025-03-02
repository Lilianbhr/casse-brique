import pygame
pygame.init()

# Fenêtre
gap = 50
largeur = 2 * gap + 800
hauteur = gap + 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Casse Brique")
bg = pygame.Color(20, 20, 20)

clock = pygame.time.Clock()
running = True
while running :
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    pygame.display.flip()
    clock.tick(60)

pygame.quit()