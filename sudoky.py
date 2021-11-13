# generate random integer values
from random import seed
from random import randint

A = [[5,1,7,6,0,0,0,3,4],
     [2,8,9,0,0,4,0,0,0],
     [3,4,6,2,0,5,0,9,0],
     [6,0,2,0,0,0,0,1,0],
     [0,3,8,0,0,6,0,4,7],
     [0,0,0,0,0,0,0,0,0],
     [0,9,0,0,0,0,0,7,8],
     [7,0,3,4,0,0,5,6,0],
     [0,0,0,0,0,0,0,0,0]]




def get_tabuleiro(tab):
 puzzle = ''
 state = False
 for a in range(0, len(tab)):
    if state:
        puzzle = puzzle + '\n-----------\n'
    state = True
    for b in range(0, len(tab)):
        
        if tab[a][b] == 0:
            puzzle = puzzle + '   ' + '|'
                
        elif  tab[a][b] != 0:
            puzzle = puzzle + str(tab[a][b]) + '|'
    return puzzle
    
get_tabuleiro(A)