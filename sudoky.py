# generate random integer values
from random import seed
from random import randint

#funcao responsavel por retornar a coluna atual
def get_coluna(tab, n):
    col = []
    for a in range(0,len(tab)):
        col.append(tab[a][n])
    return col

#funcao responsavel por retornar a celula atual
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

#funcao responsavel concluir se e possivel ou nao colocar um numero de 0 a 9 numa certa entrada do grid
def is_safe(grid,row,col,n):
    if (n not in grid[row]) and (n not in get_coluna(grid,col)) and (n not in get_celula(grid,row,col)) :
        return True
    else:
        return False

#verifica se existe um zero no grid, ou seja, um lugar no grid que ainda nao foi preenchido
def empty_spot(grid,l):
    for row in range(0, len(grid)):
        for col in range(0, len(grid)):
            if (grid[row][col] == 0):
                l[0]= row
                l[1]= col
                return True
    return False     
   
#funcao que resolve o sudoko
def solver(grid):
    l =[0, 0] #inicializacao do indice das linhas e das colunas

    if (empty_spot(grid,l) == False):
        return True
    
    row = l[0] #guarda o indice das linhas atraves da funcao empty_spot
    col = l[1] #guarda o indice das colunas atraves da funcao empty_spot
    
    for i in range(1, 10): #i e numero de 0 a 9

            if is_safe(grid,row,col,i) : #verifica se o numero i passa nas 
                #condicoes basicas do jogo do Sudoko: ser unico na linha, na coluna e na celula
                    
                grid[row][col] = i   #caso passe nas condicoes acima, coloca esse número i na entrada (row,col) do grid e depois 
                #chama a função solver() de novo com o grid atualizado para esta entrada e tenta-se preencher 
                # a proxima entrada que esteja a zero ate ver se e possivel preencher todo o grid.
                
                #caso se chegue a um "dead end" em que fiquem zeros por preencher e ja nao e possivel cumprir as regras, 
                #repete-se o processo todo de novo porque na linha 94 se da um reset na entrada inicial desta tentativa de grid resolvido e 
                #como isto e um for loop , logo a proxima tentativa sera diferente e serao tentadas todas as possibilidades.
        
                if(solver(grid)): #onde a recursiva ocorre,ate que um grid seja preenchido sem deixar 
                #zeros e onde se cumprem as regras basicas do jogo
                    return True
                
                grid[row][col] = 0 #isto executa o backtracking 
    return False
               
#funcao que da print do resultado obtido na funcao solver
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
