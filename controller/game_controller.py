import pygame
import random
from model.player import Player
from view.game_view import GameView

class GameController:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(x=100, y=550, width=250, height=250)
        self.view = GameView(screen)
        self.clock = pygame.time.Clock()


        self.quotes = [
            "Kupo! Adventure is just around the corner!",
            "Kupo! Don’t forget to take a break every now and then!",
            "Kupo! The world is full of surprises!",
            "Kupo! Trust in your heart and the path will appear!",
            "Kupo! A nap can solve anything, kupo!",
            "Kupo! Believe in the power of friendship!",
            "Kupo! Treasure is hidden where you least expect it!",
            "Kupo! Dreams are the wings that carry you far!",
            "Kupo! Even a little Moogle can do great things!",
            "Kupo! Keep your eyes on the stars, but your feet on the ground!",
            "Kupo! A good deed never goes unrewarded, kupo!",
            "Kupo! Let’s find some treasure, kupo!",
            "Kupo! Even the smallest things can bring the biggest joy!",
            "Kupo! Follow the wind and you’ll find your way!",
            "Kupo! The sky’s the limit, kupo!",
            "Kupo! Magic is everywhere, if you know where to look!"
        ]
        self.dialogue_timer = 0
        self.dialogue_display_time = 400
        self.dialogue_cycle_time = 1800
        self.current_quote = random.choice(self.quotes)  
        self.font = pygame.font.Font(None, 36)
        self.show_dialogue = False

        pygame.mixer.music.load("assets/Beyond The Final Days.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.is_muted = False
        self.mute_icon = pygame.image.load("assets/mute.png").convert_alpha()
        self.unmute_icon = pygame.image.load("assets/unmute.png").convert_alpha()
        self.mute_icon = pygame.transform.scale(self.mute_icon, (50, 50))
        self.unmute_icon = pygame.transform.scale(self.unmute_icon, (50, 50))
    def update_dialogue(self):
        self.dialogue_timer += 1

        if self.dialogue_timer > self.dialogue_cycle_time:
            self.dialogue_timer = 0
            self.current_quote = random.choice(self.quotes)
            self.show_dialogue = True

        if self.show_dialogue and self.dialogue_timer > self.dialogue_display_time:
            self.show_dialogue = False

    def draw_dialogue(self):
         if self.show_dialogue:
            
            text_surface = self.font.render(self.current_quote, True, (255, 255, 255)) 
            text_rect = text_surface.get_rect(topleft=(10, self.screen.get_height() - 50))

            background_rect = pygame.Rect(
                text_rect.x - 10, text_rect.y - 5,  
                text_rect.width + 20, text_rect.height + 20
            )
            pygame.draw.rect(self.screen, (50, 50, 100, 180), background_rect)

            
            self.screen.blit(text_surface, text_rect)

    def draw_mute_button(self):
        
        icon = self.mute_icon if self.is_muted else self.unmute_icon
        icon_rect = icon.get_rect(topright=(self.screen.get_width() - 42, 10))

    
        background_rect = pygame.Rect(icon_rect.x - 2, icon_rect.y - 2, icon_rect.width + 4, icon_rect.height + 4)
        pygame.draw.rect(self.screen, (255, 255, 255), background_rect)

        
        self.screen.blit(icon, icon_rect)

        return icon_rect

    def handle_mute_toggle(self, pos):
        icon_rect = self.draw_mute_button()
        if icon_rect and icon_rect.collidepoint(pos):
            self.is_muted = not self.is_muted
            print(f"Toggled is_muted: {self.is_muted}")
            if self.is_muted:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()

            
            self.draw_mute_button()
            pygame.display.update()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mute_toggle(event.pos)

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            self.update_dialogue()

            self.view.draw_background()
            self.view.draw_player(self.player)
            self.draw_dialogue()
            self.draw_mute_button()
            self.view.update_display()

            self.clock.tick(60)