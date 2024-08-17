import pygame

class GameView:
    def __init__(self, screen):
        self.screen = screen

    def draw_background(self):
        self.screen.fill((135, 206, 233))  #SKY COLOR

    def draw_player(self, player):
        pygame.draw.rect(self.screen, player.color, player.rect)

    def update_display(self):
        pygame.display.flip()            