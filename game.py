# import module
import pygame
from title_screen import TitleScreen

class Main:
    def __init__(self):
        # initialize pygame
        pygame.init()

        # display the screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("tetris")

        self.entities()

        self.run_title_screen()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

    def run_title_screen(self):
        while True:
            title_page = TitleScreen()
            title_page.title_loop()
            if title_page.play_selected:
                self.run_game()
                break
            else:
                pygame.quit()
                exit()
            
    def run_game(self):        
        self.clock = pygame.time.Clock()
        
        keepGoing = True 
        while keepGoing: 

            self.clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

Main()