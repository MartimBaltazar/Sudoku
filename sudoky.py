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

def get_coluna(tab, n):
    col = []
    for a in range(0,len(tab)):
        col.append(tab[a][n])
     
    print(col)    
    return col

        
    
    

def code(tab):
    
    i = 1
    for a in range(0, len(tab)):
        for b in range(0, len(tab)):
            if tab[a][b] == 0 and (i not in tab[a]) and i not in get_coluna(tab,b) :
                tab[a][b] = i
            else:
                i += 1
    return tab
    
                
            



def get_tabuleiro(tab):
    puzzle = ''
    state = False
    for a in range(0, len(tab)): #percorrer a matriz tab
        if state and ((a) % 3 == 0 and a != 0): #condição para só criar uma barra de três em três números
            
            puzzle = puzzle + '\n--------------------------------\n'
            
        elif state:
            
            puzzle = puzzle + '\n'
            
        state = True
        for b in range(0, len(tab)): #percorrer as listas de dentro da matriz tab
            if ((b+1) % 3 == 0 and b != 0):
                
                if tab[a][b] == 0:
                    puzzle = puzzle + ' 0' + ' | '
                        
                elif  tab[a][b] != 0:
                    puzzle = puzzle + ' ' + str(tab[a][b]) + ' | '
            else:
                
                if tab[a][b] == 0:
                        puzzle = puzzle + ' 0' + ' '
                        
                elif  tab[a][b] != 0:
                    puzzle = puzzle + ' ' + str(tab[a][b]) + ' '
    print(puzzle)
    return puzzle

    
get_tabuleiro(A)
get_coluna(A,3)
