
import pygame
import Pong2

def main():
    pygame.init()

    FPS = 30
    clock = pygame.time.Clock()


    WORLDSIZE = 600
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    
    size = [WORLDSIZE, WORLDSIZE]
    screen = pygame.display.set_mode(size)
    
    titleFont = pygame.font.SysFont("monospace", 35)
    myFont = pygame.font.SysFont("monospace", 20)
    smallFont = pygame.font.SysFont("monospace", 15)
    
    welcome = titleFont.render("Welcome to My Arcade!", 1, WHITE)
    choose = myFont.render("Type a number to choose a game.", 1, WHITE)
    game1 = myFont.render("1. Pong", 1, WHITE)
    note = smallFont.render("More to be added soon!", 1, WHITE)

    done = False
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Pong2.main()
                    
        screen.fill(BLACK)

        screen.blit(welcome,(90, 200))
        screen.blit(choose, (120, 250))
        screen.blit(game1, (250, 290))
        screen.blit(note, (190, 500))
        
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
