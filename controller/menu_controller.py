import pygame
import sys
import time
import math

class MenuController:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 54)
        self.menu_options = ["Start Game", "Settings", "Quit Game"]
        self.selected_option = 0

        self.background_image = pygame.image.load("assets/menu_bg.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (screen.get_width(), screen.get_height()))

        self.logo_image = pygame.image.load("assets/logo.png").convert_alpha()
        self.logo_image = pygame.transform.scale(self.logo_image, (550, 550))

        self.logo_final_y = -100
        self.logo_opacity = 0
        self.logo_fade_in_duration = 10
        self.background_opacity = 0
        self.fade_in_duration = 50
        self.start_time = time.time()


    def draw_menu(self):
        
        elapsed_time = time.time() - self.start_time

        if elapsed_time < self.fade_in_duration:
            self.background_opacity = int((elapsed_time / self.fade_in_duration) * 255)
        else:
            self.background_opacity = 255

        
        background = self.background_image.copy()
        background.set_alpha(self.background_opacity)
        self.screen.blit(background, (0, 0))

        if elapsed_time < self.logo_fade_in_duration:
            self.logo_opacity = int((elapsed_time / self.logo_fade_in_duration) * 255)
        else:
            self.logo_opacity = 255

        logo = self.logo_image.copy()
        logo.set_alpha(self.logo_opacity)
        logo_x_position = self.screen.get_width() // 2 - self.logo_image.get_width() // 2
        self.screen.blit(logo, (logo_x_position, self.logo_final_y))

        base_y = self.logo_final_y + 500
        for i, option in enumerate(self.menu_options):
            if i == self.selected_option:
                label = self.font.render(option, True, (0, 0, 0))  
                fluctuation = 1.05 + 0.05 * math.sin(time.time() * 4) 
                label = pygame.transform.scale(label, (int(label.get_width() * fluctuation), int(label.get_height() * fluctuation)))
            else:
                label = self.font.render(option, True, (100, 100, 100)) 

            label_rect = label.get_rect(center=(self.screen.get_width() // 2, base_y + i * 100))
            self.screen.blit(label, label_rect)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
            pygame.time.wait(150) 
        elif keys[pygame.K_UP]:
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
            pygame.time.wait(150)
        elif keys[pygame.K_RETURN]:
            if self.menu_options[self.selected_option] == 'Start Game':
                return 'start_game'
            elif self.menu_options[self.selected_option] == 'Settings':
                return 'settings'
            elif self.menu_options[self.selected_option] == 'Quit Game':
                pygame.quit()
                sys.exit()
    def run_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            action = self.handle_input()
            if action == 'start_game':
                return 'start_game'

            self.draw_menu()
            pygame.display.flip()
