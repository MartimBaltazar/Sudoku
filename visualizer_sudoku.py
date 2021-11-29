import pygame
import os
import time
from sudoky import criar_tabuleiro

pygame.font.init()
pygame.mixer.init()

# Set window resolution
dif = 500/9
WIDTH, HEIGHT = 500,500
CENTER = WIDTH // 2 - 100
WHITE =(255,255,255)
BLACK =(0,0,0)
RANDOM = (100,255,100)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("SUDOKU")
img = pygame.image.load('image2.png')
pygame.display.set_icon(img)

# Generate Sudoku Board.
#grid = criar_tabuleiro(2)
 
# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 70)

def draw_menu(level1,level2,level3):
    TITLE = pygame.Rect(CENTER,50,200,50)
    pygame.draw.rect(WIN,RANDOM,TITLE,0)
    pygame.draw.rect(WIN,BLACK,level1,0)
    pygame.draw.rect(WIN,BLACK,level2,0)
    pygame.draw.rect(WIN,BLACK,level3,0)
    text0 = font2.render("SUDOKU", True, BLACK)
    text1 = font1.render("EASY", True, WHITE)
    text2 = font1.render("MEDIUM", True, WHITE)
    text3 = font1.render("HARD", True, WHITE)
    WIN.blit(text0,TITLE)
    WIN.blit(text1,level1)
    WIN.blit(text2,level2)
    WIN.blit(text3,level3)
    
def draw_grid(grid):
    WIN.fill(WHITE) #restore screen
    for i in range (9):
        for j in range (9):
            # Fill grid 
            number = font1.render(str(grid[i][j]), 1, (0, 0, 0))
            WIN.blit(number, (i * dif + 15, j * dif + 15))
    # Draw lines horizontally and vertically to form grid          
    for i in range(10):
        if i % 3 == 0 :
            thick = 6
        else:
            thick = 2
        pygame.draw.line(WIN, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(WIN, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)     

def main():
    WIN.fill(RANDOM)
    EASY = pygame.Rect(CENTER,175, 200,50)
    MEDIUM = pygame.Rect(CENTER, 275, 200, 50)
    HARD = pygame.Rect(CENTER, 375, 200, 50)
    draw_menu(EASY,MEDIUM,HARD)
    state = True
    run = True
    while run:
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
                    state = False
        pygame.display.update()
    pygame.quit()

main()