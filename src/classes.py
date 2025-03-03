import pygame

total = pygame.sprite.Group()
briques = pygame.sprite.Group()

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/Paddle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (120, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.centery = 820
        self.direction = 0
        self.speed = 13

        total.add(self)

    def update(self):
        current_x = self.rect.x

        if self.direction == 1 :
            self.rect.x += self.speed
        elif self.direction == -1 :
            self.rect.x -= self.speed

        if self.rect.left < 0 or self.rect.right > 900:
            self.rect.left = current_x

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../assets/images/Ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (13, 13))
        self.rect = self.image.get_rect()
        self.rect.centerx = 450
        self.rect.centery = 425
        self.speed = [1, 9]
        self.bounce = pygame.mixer.Sound("../assets/musique/bounce.mp3")
        self.bounce.set_volume(1)
        self.bick_break = pygame.mixer.Sound("../assets/musique/break.mp3")
        self.bick_break.set_volume(1)

        total.add(self)

    def update(self, paddle_direction):
        current_x = self.rect.x
        current_y = self.rect.y
        current_speed = self.speed

        if self.rect.left <= 0 or self.rect.right >= 900:
            self.rect.x = current_x
            self.speed[0] *= -1
            self.bounce.play()
        if self.rect.top <= 0 :
            self.rect.y = current_y
            self.speed[1] *= -1
            self.bounce.play()

        liste_collision = pygame.sprite.spritecollide(self, total, False)
        for elt in liste_collision :
            if type(elt) == Paddle :
                self.bounce.play()
                self.speed[0] += paddle_direction
                self.speed[1] = 10 - abs(self.speed[0])
                self.rect.bottom = elt.rect.top + 3
                self.speed[1] *= -1
            elif type(elt) == Brick :
                self.bick_break.play()
                if (self.rect.top <= elt.rect.bottom and self.rect.bottom > elt.rect.bottom) or (self.rect.bottom >= elt.rect.top and self.rect.top < elt.rect.top):
                    self.speed[1] *= -1
                if (self.rect.right >= elt.rect.left and self.rect.left < elt.rect.left) or (self.rect.left <= elt.rect.right and self.rect.right > elt.rect.right):
                    self.speed[0] *= -1
                elt.kill()

        if abs(self.speed[0]) + abs(self.speed[1]) != 10 :
            self.speed = current_speed

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

class Brick(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (80, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        briques.add(self)
        total.add(self)