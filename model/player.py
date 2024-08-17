import pygame
import math

class Player:
    def __init__(self, x, y, width, height):
        self.image = pygame.image.load("assets/moogle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        print(f"Initial position: {self.rect.topleft}")
        self.velocity = 5
        self.jump_velocity = 10
        self.gravity = 0.5
        self.is_jumping = False
        self.y_velocity = 0
        self.facing_right = True

        self.fluctuation_amplitude = 8
        self.fluctuation_speed = 0.05
        self.fluctuation_phase = 0
        self.base_y= y
        

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
            if self.facing_right:
                self.facing_right = False
                self.image = pygame.transform.flip(self.image, True, False)

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
            if not self.facing_right:
               self.facing_right = True
               self.image = pygame.transform.flip(self.image, True, False)

        if self.rect.x < 0:
            self.rect.x = 0 
        if self.rect.x > 1080 - self.rect.width:
            self.rect.x = 1080 - self.rect.width

        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
                self.y_velocity = -self.jump_velocity

        self.rect.y += self.y_velocity
        if self.is_jumping:
            self.y_velocity += self.gravity

        if self.rect.y >= 650 - self.rect.height:  #IMPORTANT!! => Ground Level is 540
            self.rect.y = 650 - self.rect.height
            self.is_jumping = False  
            self.y_velocity = 0  
            self.base_y = self.rect.y   

        if not self.is_jumping:
            self.apply_fluctuation()

    def apply_fluctuation(self):
        self.fluctuation_phase += self.fluctuation_speed
        if self.fluctuation_phase > 2 * math.pi:
            self.fluctuation_phase <= 2 * math.pi

        fluctuation_offset = math.sin(self.fluctuation_phase) * self.fluctuation_amplitude

        self.rect.y = self.base_y + fluctuation_offset                     