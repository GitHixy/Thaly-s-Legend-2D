import pygame
from controller.game_controller import GameController

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Thaly's Legend 2D")

    game_controller = GameController(screen)
    game_controller.run_game()

if __name__ == "__main__":
    main()    