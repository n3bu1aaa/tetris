# import module
import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action 

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        font = pygame.font.Font("fonts/alternate_font.otf", 25)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if self.rect.collidepoint(event.pos):  
                if self.action:
                    self.action() 
