# generate random integer values
from random import seed
from random import randint

def get_coluna(tab, n):
    col = []
    for a in range(0,len(tab)):
        col.append(tab[a][n])
     

    return col

def get_celula(tab, l1,c1):
    cel = []
    il = 0
         
    if 0 <= l1 < 3:
        il = 0 
        jl = 3
    if 0 <= c1 < 3:
        ic = 0 
        jc = 3
    if 3 <= l1 < 6:
        il = 3 
        jl = 6
        
    if 3 <= c1 < 6:
        ic = 3 
        jc = 6
    
    if 6 <= l1 <=8:
        il = 6 
        jl = 9
        
    if 6 <= c1 <= 8:
        ic = 6 
        jc = 9
    
    
        
    for a in range(il,jl):
        for b in range(ic,jc):
            cel.append(tab[a][b])
     
    
    return cel
   
#get_celula(A,5,5)

def is_safe(grid,row,col,n):
    
    if (n not in grid[row]) and (n not in get_coluna(grid,col)) and (n not in get_celula(grid,row,col)) :
        return True
    else:
        return False
    
def empty_spot(grid,l):
    
    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            if (grid[row][col] == 0):
                l[0]= row
                l[1]= col
                return True
    return False     
   

def solver(tab):
    
    l =[0, 0]
    
    if (empty_spot(tab,l) == False):
        return True
    
    row = l[0]
    col = l[1]  
    
    for i in range(1, 10):

            if is_safe(tab,row,col,i) :
                    
                tab[row][col] = i   
        
                if(solver(tab)):
                    return True
                
                tab[row][col] = 0
             
        
    return False
               

def get_tabuleiro(tab):
    puzzle = ''
    state = False
    for a in range(0, len(tab)): #percorrer a matriz tab
        if state and ((a % 3 == 0) and a != 0): #condicao para so criar uma barra de tres em tres numeros
            
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

    
#lsd = solver(A) 
#get_tabuleiro(lsd)

if __name__=="__main__":
    
    A =[[0 for x in range(9)]for y in range(9)]
    
    A = [[5,1,7,6,0,0,0,3,4],
     [2,0,9,0,0,4,0,0,0],
     [3,4,6,2,0,5,0,9,0],
     [6,0,2,0,0,0,0,1,0],
     [0,3,8,0,0,6,0,4,7],
     [0,0,0,0,0,0,0,0,0],
     [0,9,0,0,0,0,0,7,8],
     [7,0,3,4,0,0,5,6,0],
     [0,0,0,0,0,0,0,0,0]]
      
    if(solver(A)):
            get_tabuleiro(A)
    else:
            print("No solution exists")