import pygame
from random import randint
from random import choice
from math import fabs

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WORLDSIZE = 600
class Ship:
    def __init__(self, x, y, window):
        w = 10
        h = 30
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

        self.vel = 5
        self.point = 0
        self.icon = pygame.draw.rect(window, WHITE, (x, y, w, h))

    def moveUp(self):
        self.y1 = self.y1 - self.vel
        self.y2 = self.y2 - self.vel
        self.icon.move_ip(0, -self.vel)

    def moveDown(self):
        if self.y2 < WORLDSIZE:
            self.y1 = self.y1 + self.vel
            self.y2 = self.y2 + self.vel
            self.icon.move_ip(0, self.vel)
    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.icon)
        
class Asteroid:
    
    def __init__(self, x, y, v, window):
        w = 8
        h = 4
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.point = 0
        self.vel = v
        self.icon = pygame.draw.rect(window, WHITE, ((x, y), (w, h)))
        
    def move(self):
        self.x1 = self.x1 + self.vel
        self.x2 = self.x2 + self.vel
        self.icon.move_ip(self.vel, 0)
        
    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.icon)
   
        
def main():
    pygame.init()
    clock = pygame.time.Clock()
    FPS = 30

    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    #Screensize
    WORLDSIZE = 600
    
    win = pygame.display.set_mode((WORLDSIZE, WORLDSIZE))
    pygame.display.set_caption("Astro Race")

    playing = True
    AsteroidList = []
                  
    P1 = Ship(200, 560, win)
    P2 = Ship(390, 560, win)
    win.fill(BLACK)
    for i in range(0,23):
        y = randint(0, 500)
        x = randint(0, 552)
        v = 5
        v = v * choice([-1,1])
        newAst = Asteroid(x, y, v, win)
        AsteroidList.append(newAst)
        AsteroidList[i].draw(win)
    
  
    P1.draw(win)
    P2.draw(win)
    pygame.display.update()
    pygame.time.wait(1000)
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                
   
                
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            P1.moveUp()
        
        elif key[pygame.K_s]:
            P1.moveDown()
        
        if key[pygame.K_UP]:
            P2.moveUp()
        elif key[pygame.K_DOWN]:
            P2.moveDown()
            
        for i in AsteroidList:
            i.move()
            i.draw(win)

                
        win.fill(BLACK)
        
        P1.draw(win)
        P2.draw(win)
        for i in range(0,len(AsteroidList) - 1):
            if AsteroidList[i].x2 <= 0 and AsteroidList[i].vel < 0:
                y = randint(0, 500)
                AsteroidList[i] = Asteroid(552, y, -5, win)
            elif AsteroidList[i].x1 >= 600 and AsteroidList[i].vel > 0:
                y = randint(0, 500)
                AsteroidList[i] = Asteroid(0, y, 5, win)
            AsteroidList[i].draw(win)

        for a in AsteroidList:
            if a.x1 >= P1.x1 and a.x1 <= P1.x2 and a.y1 >= P1.y1 and a.y1 <= P1.y2:
                P1 = Ship(200, 560, win)
                P1.draw(win)
            elif a.x1 >= P2.x1 and a.x1 <= P2.x2 and a.y1 >= P2.y1 and a.y1 <= P2.y2:
                P2 = Ship(390, 560, win)
                P2.draw(win)
                
        if P1.y1 <= 0:
            P1.point += 1
            P1 = Ship(200, 560, win)
            P1.draw(win)
            
        if P2.y1 <= 0:
            P2.point += 1
            P2 = Ship(390, 560, win)
            P2.draw(win)
            
        clock.tick(FPS)
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    main()
