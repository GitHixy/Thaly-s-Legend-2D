import pygame


class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.velocity = 5
        self.jump_velocity = 10
        self.gravity = 0.5
        self.is_jumping = False
        self.y_velocity = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
                self.y_velocity = -self.jump_velocity

        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += self.gravity
            if self.rect.y >= 540:  #IMPORTANT!! => Ground Level is 540
                self.rect.y = 540
                self.is_jumping = False                    