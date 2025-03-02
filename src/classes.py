import pygame

total = pygame.sprite.Group()
briques = pygame.sprite.Group()

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/Paddle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.centery = 820
        self.direction = 0
        self.speed = 10

        total.add(self)

    def update(self):
        current_x = self.rect.x

        if self.direction == 1 :
            self.rect.x += self.speed
        elif self.direction == -1 :
            self.rect.x -= self.speed

        if self.rect.left < 0 or self.rect.right > 900:
            self.rect.left = current_x