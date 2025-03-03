import pygame
from classes import *
pygame.init()
pygame.mixer.init()

# Fenêtre
gap = 50
largeur = 2 * gap + 800
hauteur = gap + 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Casse Brique")
bg = pygame.Color(20, 20, 20)

paddle = Paddle()
ball = Ball()

choix_image = {
    "R": pygame.image.load("../assets/images/Brick-Red.png").convert_alpha(),
    "O": pygame.image.load("../assets/images/Brick-Orange.png").convert_alpha(),
    "J": pygame.image.load("../assets/images/Brick-Yellow.png").convert_alpha(),
    "V": pygame.image.load("../assets/images/Brick-Green.png").convert_alpha(),
    "B": pygame.image.load("../assets/images/Brick-Blue.png").convert_alpha()
}

def dessiner_niveau():
    fichier = open("../levels/level_2.txt", "r")
    lignes = fichier.readlines()
    y = 0
    for ligne in lignes :
        x = 0
        for elt in ligne :
            if elt in choix_image :
                brique = Brick(choix_image[elt], x + gap, y + gap)
            x += 80
        y += 20

dessiner_niveau()

# Musique
musique = pygame.mixer.music.load("../assets/musique/main-theme.mp3")
pygame.mixer.music.set_volume(0.2)
perdu = pygame.mixer.Sound("../assets/musique/lose.mp3")
perdu.set_volume(1)
gagne = pygame.mixer.Sound("../assets/musique/win.mp3")
perdu.set_volume(1)

pygame.mixer.music.play(3)
clock = pygame.time.Clock()
running = True
while running :
    screen.fill(bg)
    ball.update(paddle.direction)
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
    if ball.rect.y > hauteur - 35 :
        running = False
        pygame.mixer.music.stop()
        perdu.play()
        pygame.time.wait(500)
    if len(briques) == 0 :
        running = False
        pygame.mixer.music.stop()
        gagne.play()
        pygame.time.wait(5000)
    pygame.display.flip()
    clock.tick(60)
pygame.time.wait(500)
pygame.quit()