import pygame
from model.player import Player
from view.game_view import GameView

class GameController:
    def __init__(self, screen):
        self.player = Player(x=375, y=540, width=50, height=50, color=(255, 0, 0))
        self.view = GameView(screen)
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            self.view.draw_background()
            self.view.draw_player(self.player)
            self.view.update_display()

            self.clock.tick(60)        