import pygame

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.background = pygame.image.load("assets/bg1.webp").convert()
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_player(self, player):
        self.screen.blit(player.image, player.rect)

    def update_display(self):
        pygame.display.flip()            