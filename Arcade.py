
import pygame
import Pong2
import AstroRace
import sys

def main():
    #initialize pygame
    pygame.init()

    #set up clock and fps
    FPS = 30
    clock = pygame.time.Clock()


    #final variables initialized
    WORLDSIZE = 600
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    #setting up window
    size = [WORLDSIZE, WORLDSIZE]
    screen = pygame.display.set_mode(size)

    #initializing fonts
    titleFont = pygame.font.SysFont("monospace", 35)
    myFont = pygame.font.SysFont("monospace", 20)
    smallFont = pygame.font.SysFont("monospace", 15)
    
    welcome = titleFont.render("Welcome to My Arcade!", 1, WHITE)
    choose = myFont.render("Type a number to choose a game.", 1, WHITE)
    game1 = myFont.render("1. Pong", 1, WHITE)
    game2 = myFont.render("2. AstroRace", 1, WHITE)
    note = smallFont.render("More to be added soon!", 1, WHITE)

    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Pong2.main()
                if event.key == pygame.K_2:
                    AstroRace.main()
                    
        screen.fill(BLACK)

        screen.blit(welcome,(90, 200))
        screen.blit(choose, (120, 250))
        screen.blit(game1, (230, 290))
        screen.blit(game2, (205, 330))
        screen.blit(note, (190, 500))
        
        clock.tick(FPS)
        pygame.display.flip()
    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    main()
