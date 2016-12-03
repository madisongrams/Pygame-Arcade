import pygame
from random import randint
from random import choice
from math import fabs
import Arcade

#global variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WORLDSIZE = 600

#class for Ship Objects
class Ship:
    #initialize location and point values
    def __init__(self, x, y, window, p = 0):
        w = 10
        h = 30
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

        self.vel = 5
        self.point = p
        self.icon = pygame.draw.rect(window, WHITE, (x, y, w, h))


    def moveUp(self):
        self.y1 = self.y1 - self.vel
        self.y2 = self.y2 - self.vel
        self.icon.move_ip(0, -self.vel)

    def moveDown(self):
        #Checks to make sure you player can move down 
        if self.y2 < WORLDSIZE:
            self.y1 = self.y1 + self.vel
            self.y2 = self.y2 + self.vel
            self.icon.move_ip(0, self.vel)
    #Allows for object to draw itself on the screen        
    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.icon)
#Class for Asteroid Objects        
class Asteroid:
    #initialize location and velocity
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
    #Allows for object to draw itself on the screen     
    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.icon)

#Class for the middle bar keeping track of a 2 minute timer  
class TimeBar:
    #initialized at full height of screen
    def __init__(self, window):
        self.y = 0
        self.count = 0
        self.icon = pygame.draw.line(window, WHITE, (300, self.y), (300, 600), 10)
    #every frame, the count updates itself
    #Since the game is set to 30 frames/second, the timer will go down by 5px a second
    def update(self, window):
        self.count += 1
        if self.count == 29:
            self.y += 5
            self.icon = pygame.draw.line(window, WHITE, (300, self.y), (300, 600), 10)
            self.count = 0
        else:
            pygame.draw.line(window, WHITE, (300, self.y), (300, 600), 10)
    #returns true when the timer has ended up        
    def isDone(self):
        return self.y == 600
#Main game method    
def main():
    #initialize pygame
    pygame.init()
    #initialize clock
    clock = pygame.time.Clock()
    FPS = 30

    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    #Screensize
    WORLDSIZE = 600

    #initialize window
    win = pygame.display.set_mode((WORLDSIZE, WORLDSIZE))
    pygame.display.set_caption("Astro Race")

    #Initialize Fonts
    scorefont = pygame.font.SysFont("ocraextended", 50)
    titleFont = pygame.font.SysFont("ocraextended", 30) 
    instrFont = pygame.font.SysFont("monospace", 20)

    #Startup Text
    title = titleFont.render("Welcome to AstroRace!", 1, WHITE)
    instr1 = instrFont.render("Race your opponent to the top, avoiding asteroids!", 1, WHITE)
    instr2 = instrFont.render("Whoever makes it to the top the most times", 1, WHITE)
    instr21 = instrFont.render("at the end of 2 minutes wins!", 1, WHITE)
    instr3 = instrFont.render("P1 Up: W, Down: S", 1, WHITE)
    instr4 = instrFont.render("P2 Up: Up Arrow, Down: Down Arrow", 1, WHITE)
    instr5 = instrFont.render("Press any key to begin!", 1, WHITE)

    #Game opens up to menu before gameplay begins
    menu = True
    playing = False
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                
            elif event.type == pygame.KEYDOWN:
                #When any key is pressed, gameplay begins
                menu = False
                playing = True
                    
        
        #updating screen
        win.fill((0, 0, 0))
        
        win.blit(title, (100, 200))
        win.blit(instr1, (0, 250))
        win.blit(instr2, (60, 290))
        win.blit(instr21, (100, 330))
        win.blit(instr3, (200, 370))
        win.blit(instr4, (140, 400))
        win.blit(instr5, (138, 450))
        
        pygame.display.update()
        clock.tick(FPS)

    #Initializing Game objects

    #asteroid objects are stored in a list
    AsteroidList = []
    
    point1 = 0
    point2 = 0
    #Initialize ships      
    P1 = Ship(200, 560, win)
    P2 = Ship(390, 560, win)
    #Initialize scores
    P1Score = scorefont.render(str(P1.point), 1, WHITE)
    P2Score = scorefont.render(str(P2.point), 1, WHITE)
    #Initialize timer
    bar = TimeBar(win)
    
    win.fill(BLACK)
    #Filling asteroid list and drawing them on the screen
    for i in range(0,23):
        y = randint(0, 500)
        x = randint(0, 552)
        v = 5
        v = v * choice([-1,1])
        newAst = Asteroid(x, y, v, win)
        AsteroidList.append(newAst)
        AsteroidList[i].draw(win)
    #Drawing scores, ships and timer on the screen
    win.blit(P1Score, (150, 550))
    win.blit(P2Score, (425, 550))
    P1.draw(win)
    P2.draw(win)
    bar.update(win)
    pygame.display.update()
    #Pause before gameplay begins
    pygame.time.wait(1000)
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                
       
        #Checking if user has inputted keys for movement       
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            P1.moveUp()
        
        elif key[pygame.K_s]:
            P1.moveDown()
        
        if key[pygame.K_UP]:
            P2.moveUp()
        elif key[pygame.K_DOWN]:
            P2.moveDown()

        #Moving asteroids
        for i in AsteroidList:
            i.move()
            i.draw(win)

        #Updating screen        
        win.fill(BLACK)
        
        P1.draw(win)
        P2.draw(win)
        bar.update(win)

        #End game case
        if bar.isDone():
            if P1.point > P2.point:
                won = instrFont.render("P1 wins!", 1,(255, 255, 255))
            elif P2.point > P1.point:
                won = instrFont.render("P2 wins!", 1,(255, 255, 255))
            else:
                won = instrFont.render("It's a tie!", 1,(255, 255, 255))
            win.fill(BLACK)
            for i in AsteroidList:
                i.draw(win)
            P1.draw(win)
            P2.draw(win)
            win.blit(won, (260, 300))
            pygame.display.update()

            #Wait a few seconds before exiting game
            pygame.time.wait(3000)
            playing = False

        #Checks for each asteroid to see if it has gone offscreen and
            #replaces them with a new asteroid
        for i in range(0,len(AsteroidList) - 1):
            if AsteroidList[i].x2 <= 0 and AsteroidList[i].vel < 0:
                y = randint(0, 500)
                AsteroidList[i] = Asteroid(552, y, -5, win)
            elif AsteroidList[i].x1 >= 600 and AsteroidList[i].vel > 0:
                y = randint(0, 500)
                AsteroidList[i] = Asteroid(0, y, 5, win)
            AsteroidList[i].draw(win)

        #Collision checks for asteroids and ships
        for a in AsteroidList:
            if a.x1 >= P1.x1 and a.x1 <= P1.x2 and a.y1 >= P1.y1 and a.y1 <= P1.y2:
                P1 = Ship(200, 560, win, point1)
                P1.draw(win)
            elif a.x1 >= P2.x1 and a.x1 <= P2.x2 and a.y1 >= P2.y1 and a.y1 <= P2.y2:
                P2 = Ship(390, 560, win, point2)
                P2.draw(win)
        #Giving players points who have reached the top of the screen        
        if P1.y1 <= 0:
            point1 = P1.point + 1
            P1 = Ship(200, 560, win, point1)
            P1.draw(win)
            P1Score = scorefont.render(str(P1.point), 1, WHITE)
            
        if P2.y1 <= 0:
            point2 = P2.point + 1
            P2 = Ship(390, 560, win, point2)
            P2.draw(win)
            P2Score = scorefont.render(str(P2.point), 1, WHITE)
        #Updates scores    
        win.blit(P1Score, (150, 550))
        win.blit(P2Score, (425, 550))

        #Ticks Clock
        clock.tick(FPS)
        pygame.display.update()
        
    Arcade.main()
    


