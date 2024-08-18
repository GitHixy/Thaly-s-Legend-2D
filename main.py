import pygame
from controller.game_controller import GameController
from controller.menu_controller import MenuController

def main():
    pygame.init()
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Thaly's Legend 2D")

    menu_controller = MenuController(screen)
    action = menu_controller.run_menu()

    if action == "start_game":
        game_controller = GameController(screen)
        game_controller.run_game()

    pygame.quit()    

if __name__ == "__main__":
    main()    