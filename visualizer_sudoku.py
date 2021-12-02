import pygame
import os
import time
import sys
from sudoky import criar_tabuleiro,empty_spot
from sudoky import is_safe

pygame.init()
pygame.font.init()
pygame.mixer.init()

# Set window resolution
cell = 500/9
val = 0
WIDTH, HEIGHT = 500,550
CENTER = WIDTH // 2 - 100
WHITE = (255,255,255)
BLUE = (0,153,240)
BLACK = (0,0,0)
GREEN = (100,255,100)
RED = (255, 0, 0)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SUDOKU")
img = pygame.image.load('image2.png')
pygame.display.set_icon(img)
background_image = pygame.image.load("blue-background.jpg").convert()
background_sound = pygame.mixer.Sound("background.mp3")
# Load test fonts for future use

font1 = pygame.font.SysFont("pressstart2pvav7", 30)
font2 = pygame.font.SysFont("pressstart2pvav7", 50)
numbers = pygame.font.SysFont("None", 40)
font3 = pygame.font.SysFont("pressstart2pvav7", 9)
font4 = pygame.font.SysFont("Atari", 40)

def get_cord(pos):
    global x
    x = pos[0]//cell
    global y
    y = pos[1]//cell

def draw_greenval(val):
    BLANK = pygame.Rect(x * cell + 2 , y * cell + 2 , cell - 1.5, cell - 1.5)
    pygame.draw.rect(WIN,BLUE,BLANK,0)        
    text1 = numbers.render(str(val), 1, (0, 0, 0))
    WIN.blit(text1, (x * cell + 15, y * cell + 15)) 

def draw_redval(val,counter):
    text = font1.render("X " * (counter+1), 1, (255, 0, 0))
    WIN.blit(text, (20, 510)) 
    BLANK = pygame.Rect(x * cell + 2 , y * cell + 2 , cell - 1.5, cell - 1.5)
    pygame.draw.rect(WIN,RED,BLANK,0)        
    text1 = numbers.render(str(val), 1, (0, 0, 0))
    WIN.blit(text1, (x * cell + 15, y * cell + 15))
    
def draw_cross(counter):
    text = font1.render("X " * (counter+1), 1, (255, 0, 0))
    WIN.blit(text, (20, 510))     
    

def draw_menu(level1,level2,level3):
    WIN.blit(background_image, [0, 0])  
    TITLE = pygame.Rect(CENTER-40,75,200,50)
    text0 = font2.render("SUDOKU", True, WHITE)
    text1 = font1.render("EASY", True, WHITE)
    text_rect1 = text1.get_rect(center=(CENTER+100, CENTER+50))
    text2 = font1.render("MEDIUM", True, WHITE)
    text_rect2 = text2.get_rect(center=(CENTER+100, CENTER+150))
    text3 = font1.render("HARD", True, WHITE)
    text_rect3 = text3.get_rect(center=(CENTER+100, CENTER+250))
    text4 = font1.render("?", True, WHITE)
    text_rect4 = text4.get_rect(center=(440, 470))
    WIN.blit(text0,TITLE)
    WIN.blit(text1,text_rect1)
    WIN.blit(text2,text_rect2)
    WIN.blit(text3,text_rect3)
    WIN.blit(text4,text_rect4)
    
def show_commands():
    WIN.fill(WHITE)
    WIN.blit(background_image, [0, 0])
    TITLE = pygame.Rect(CENTER-65,50,250,50)
    R = pygame.Rect(CENTER-75,125, 250,20)
    CREDITS = pygame.Rect(CENTER-75, 175, 250, 20)    
    #pygame.draw.rect(WIN,GREEN,TITLE,0)
    #pygame.draw.rect(WIN,BLACK,R,0)
    #pygame.draw.rect(WIN,BLACK,CREDITS,0)
    text0 = font1.render("COMMANDS", True, WHITE)
    text1 = font3.render("- R is used to go back to the main menu", True, WHITE)
    text2 = font3.render("- Credits", True, WHITE)  
    WIN.blit(text0,TITLE)
    WIN.blit(text1,R)
    WIN.blit(text2,CREDITS)    
    
def draw_endgame(grid):
    WIN.blit(background_image, [0, 0])
    TITLE = pygame.Rect(CENTER-50,50,250,50)
    DEFEATED = pygame.Rect(CENTER,125, 250,20)    
    pygame.draw.rect(WIN,GREEN,TITLE,0)
    pygame.draw.rect(WIN,GREEN,DEFEATED,0)
    text0 = font1.render("YOU WERE DEFEATED", True, BLACK)
    text2 = font3.render("Press R to restart the game", True, BLACK)  
    WIN.blit(text0,TITLE)
    WIN.blit(text2,DEFEATED)
    draw_grid(grid)

def solver(grid,i=[0]):
    
    i[0]+=1
    l =[0, 0] #Inicializacao do indice das linhas e das colunas
    
    if (empty_spot(grid,l) == False):
        return True
    
    row = l[0] #guarda o indice das linhas atraves da funcao empty_spot
    col = l[1] #guarda o indice das colunas atraves da funcao empty_spot
    pygame.event.pump()   
    for i in range(1, 10): #i e numero de 0 a 9
            if is_safe(grid,row,col,i) : #Verifica se o numero i passa nas 
                #condicoes basicas do jogo do Sudoko: ser unico na linha, na coluna e na celula
                global x, y
                x = row
                y = col               
                grid[row][col] = i   
                WIN.fill(WHITE)
                draw_grid(grid)
                pygame.display.update()
                pygame.time.delay(25)                
                     
                if(solver(grid)):
                    return True
                
                grid[row][col] = 0 
                WIN.fill(WHITE)
                draw_grid(grid)
                draw_redval(i,2)
                pygame.display.update()
                pygame.time.delay(25)                   
                
    return False    

def draw_grid(grid):
    WIN.fill(WHITE) #restore WIN
    for i in range (9):
        for j in range (9):
            if grid[i][j]!= 0:
                pygame.draw.rect(WIN, BLUE, (i * cell, j * cell, cell + 1, cell + 1))
                number = numbers.render(str(grid[i][j]), 1, (0, 0, 0))
                WIN.blit(number, (i * cell + 15, j * cell + 15))
    # Draw lines horizontally and vertically to form grid          
    for i in range(10):
        if i % 3 == 0 :
            thick = 6
        else:
            thick = 2
        pygame.draw.line(WIN, (0, 0, 0), (0, i * cell), (500, i * cell), thick)
        pygame.draw.line(WIN, (0, 0, 0), (i * cell, 0), (i * cell, 500), thick)    


def main():
    EASY = pygame.Rect(CENTER,175, 200,50)
    MEDIUM = pygame.Rect(CENTER, 275, 200, 50)
    HARD = pygame.Rect(CENTER, 375, 200, 50)
    draw_menu(EASY,MEDIUM,HARD)
    counter = 0
    val = 0
    grid = []
    pygame.mixer.Sound.play(background_sound)
    state = True
    run = True
    while run:
        if counter == 3:
            if solver(grid) == True:
                state = True
                draw_grid(grid)
                draw_endgame(grid)
                counter = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if state:
                if event.type == pygame.MOUSEBUTTONUP:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if CENTER < mouseX < (CENTER + 200) and 175 < mouseY < 225:
                        grid = criar_tabuleiro(1)
                        draw_grid(grid)
                    if CENTER < mouseX < (CENTER + 200) and 275 < mouseY < 325:
                        grid = criar_tabuleiro(2)
                        draw_grid(grid)
                    if CENTER < mouseX < (CENTER + 200) and 375 < mouseY < 425:
                        grid = criar_tabuleiro(3)  
                        draw_grid(grid)
                    elif 425 < mouseX < 465 and 450 < mouseY < 490:
                        show_commands()           
                    state = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                get_cord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2   
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9                             
                if event.key == pygame.K_r:
                    WIN.fill(WHITE)
                    draw_menu(EASY,MEDIUM,HARD)
                    state = True 
                    counter = 0
                if val != 0:
                    if is_safe(grid,int(x),int(y),val):
                        #draw_greenbox()
                        draw_greenval(val)
                        grid[int(x)][int(y)]= val
                        val = 0
                    else:
                        #draw_redbox(counter)
                        draw_redval(val,counter)
                        counter += 1
                        val = 0     
        pygame.display.update()
    pygame.mixer.music.stop()
    pygame.display.quit()
    pygame.quit()
    sys.exit()

main()
