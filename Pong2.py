import pygame
import Arcade
from random import randint
from random import choice
from math import fabs

WORLDSIZE = 600
#class for a Paddle Object
class Paddle:
    
    #initialize its location and size
    def __init__(self, x, y, w, h, window):
        
        self.x1 = x
        self.y1 = y
        self.x2 = x + 10
        self.y2 = y + h
        self.vel = 9
        self.point = 0
        self.icon = pygame.draw.rect(window, (255,255,255), (x,y,10,h))
    
    def moveUp(self,window):
        
        #checks to see if at top of screen
        if self.y1 <= 0:
            
            self.icon.move_ip(0, 0)
            
        else:
            self.y1 = self.y1 - self.vel
            self.y2 = self.y2 - self.vel
            self.icon.move_ip(0, -self.vel)
            
    def moveDown(self,window):
        #checks to see if at bottom of screen
        if self.y2 >= WORLDSIZE:
            self.icon.move_ip(0, 0)
            
        else:
            self.y1 = self.y1 + self.vel
            self.y2 = self.y2 + self.vel
            self.icon.move_ip(0, self.vel)
            
    #Slow is supposed to called to keep from immediate stop of paddle, have not added this functionality yet        
    def Slow(self):
        
        if self.vel == 0:
            self.vel = 0
            
        else:
            self.vel -= 1
            
    #Allows object to draw itself on the screen        
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.icon)
        
class Ball:
    
    def __init__(self, x, y, w, h, window):
        
        #random direction of the ball
        self.dX = choice([-9, -8, -7, -6, 6, 7, 8, 9])
        self.dY = randint(6, 9)
        
        #random position of the ball
        y = randint(200, 400)
        
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        
        self.icon = pygame.draw.rect(window, (255, 255, 255), (x, y, w, h))
        
    #Calculating movement of ball, takes in both players as parameters to check for collisions    
    def move(self, P1, P2, window):

        #bounces off paddles
        if self.x1  <= P1.x2 and self.x1 >= P1.x1 and self.y1 >= P1.y1 and self.y2 <= P1.y2:
            self.dX = -self.dX
            
            
        elif self.x2 >= P2.x1 and self.x2  <= P2.x2 and self.y1  >= P2.y1 and self.y2 <= P2.y2:
            self.dX = -self.dX
            
        #bounces off bottom and top of screen    
        if self.y2 >= WORLDSIZE or self.y1 <= 0:
            self.dY = -self.dY
            
        self.icon.move_ip(self.dX, self.dY)

        #updates its position
        self.x1 += self.dX
        self.x2 += self.dX
        self.y1 += self.dY
        self.y2 += self.dY
        
    #Allows object to draw itself on the screen         
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.icon)

def main():
    
    pygame.init()
    
    #Creating clock and setting FPS
    fpsClock = pygame.time.Clock()
    FPS = 30
    
    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    #Screensize
    WORLDSIZE = 600
    
    #Create the window
    win = pygame.display.set_mode((WORLDSIZE, WORLDSIZE))
    pygame.display.set_caption("Pong")
   
    #Initialize fonts
    myfont = pygame.font.SysFont("monospace", 25)
    myfont2 = pygame.font.SysFont("monospace", 20)
    myfont3 = pygame.font.SysFont("ocraextended", 30)
    scorefont = pygame.font.SysFont("ocraextended", 50)
    
    #Initialize original instructions
    beg1 = myfont3.render("Welcome to Pong!", 1, WHITE)
    beg2 = myfont.render("Press 1 for 1 Player", 1, WHITE)
    beg3 = myfont.render("Press 2 for 2 Players", 1, WHITE)
    p1i = myfont2.render("P1 Up: W, Down: S", 1, WHITE)
    p2i = myfont2.render("P2 Up: Up Arrow, Down: Down Arrow", 1, WHITE)

    menu = True
    playing = False

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                
            if event.type == pygame.KEYDOWN:
                #One player Game
                if event.key == pygame.K_1:
                    Two = False
                    menu = False
                    playing = True
                #Two player Game    
                elif event.key == pygame.K_2:
                    Two = True
                    menu = False
                    playing = True
                    
        

        
        #updating screen
        win.fill((0, 0, 0))
        
        win.blit(beg1, (168, 200))
        win.blit(beg2, (160, 250))
        win.blit(beg3, (152, 290))
        win.blit(p1i, (200, 330))
        win.blit(p2i, (128, 360))
        
        pygame.display.update()
        fpsClock.tick(FPS)

    #Initialize players and ball    
    P1 = Paddle(40, 250, 30, 100, win)
    P2 = Paddle(520, 250, 30, 100, win)
    B = Ball(295, 295, 10, 10, win)
    win.fill(BLACK)
    #Initialize Score count
    
    P1Score = scorefont.render(str(P1.point), 1, WHITE)
    P2Score = scorefont.render(str(P2.point), 1, WHITE)

    win.fill(BLACK)

    #Blitting score counts
    win.blit(P1Score, (150, 50))
    win.blit(P2Score, (400, 50))
    #drawing middle line
    pygame.draw.line(win, WHITE, (300, 0), (300, 600))
    #drawing players and ball
    P1.draw(win)
    P2.draw(win)
    B.draw(win)
    #updating the screen and pausing before beginning game play
    pygame.display.update()
    pygame.time.wait(1000)
    
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #exit out of game loop
                playing = False
                
        #updating screen    
        win.fill(BLACK)
        win.blit(P1Score,(150, 50))
        win.blit(P2Score,(400, 50))
        pygame.draw.line(win, WHITE, (300,0), (300,600))
        P1.draw(win)
        P2.draw(win)
        B.draw(win)

        
        #check to see if keys are being pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            P1.moveUp(win)
        
        if key[pygame.K_s]:
            P1.moveDown(win)
            
        #if two players, allows for second player to have control of movement
        if Two == True:
            if key[pygame.K_UP]:
                P2.moveUp(win)
        
            elif key[pygame.K_DOWN]:
                P2.moveDown(win)
                
        #if single player, computer has control of second paddle
        else:
            #computer follows ball, need to make a better system for this
            P2.vel = fabs(B.dY)
            if B.y1 < P2.y1 + 50:
                P2.moveUp(win)
                
            elif B.y2 > P2.y2 - 50:
                P2.moveDown(win)
                
        #moves the ball     
        B.move(P1, P2, win)

        #checks to see if ball goes off screen on either side, giving a player a point
        if B.x2 <= 0:
            P2.point += 1
            P2Score = scorefont.render(str(P2.point), 1, WHITE)
            win.blit(P2Score, (400, 50))
            #makes a new ball
            B = Ball(295, 295, 10, 10, win)
            
            
        elif B.x1 >= WORLDSIZE:
            P1.point += 1
            P1Score = scorefont.render(str(P1.point), 1, WHITE)
            win.blit(P1Score, (150, 50))
            #makes a new ball
            B = Ball(295, 295, 10, 10, win)
            
        #checks to see if a player has won    
        if P1.point == 5 or P2.point == 5:
            win.fill((0, 0, 0))
            
            win.blit(P1Score, (150, 50))
            win.blit(P2Score, (400, 50))
            
            #looks to see who won
            
            if P1.point == 5:
                won = myfont3.render("P1 wins!", 1,(255, 255, 255))
            else:
                won = myfont3.render("P2 wins!", 1,(255, 255, 255))
                
            #updates the screen with winning text
                
            win.blit(won,(200, 300))
            pygame.display.update()
            P1.point = 0
            P2.point = 0
            #waits before exiting out of game
            pygame.time.wait(3000)
            playing = False
            
        #updating clock and display
        fpsClock.tick(FPS)
        pygame.display.update()
        
    #returns back to main arcade file once game ends
    Arcade.main()
            
        
    
