import cv2
import pytesseract
import imutils
import cv2
from ai_sudoku_reader import*

def main_ai():
    image_path = 'oi.png'

    image_pre_AI = grid_pronto_para_AI(image_path)
    image_pre_AI_2 = cv2.resize(image_pre_AI, (450,450))

    grid = np.zeros([int(9),int(9)])
    c = 0
    d = 0
    for i in range(9):
            for j in range(9):
                quadrado_atual = image_pre_AI_2[(int(450*(i)/9))+3:(int((450*(i+1))/9))-3,(int((450*(j))/9))+3:(int((450*(j+1))/9))-3]
                
                
                number_of_white_pix = cv2.countNonZero(quadrado_atual)
                number_of_black_pix = 2500 - number_of_white_pix  
                #print(number_of_black_pix)
                if number_of_black_pix > 2400 :
        
                    grid[i][j] = int(0)
                    
                else:
                
                    image_resize = cv2.resize(quadrado_atual, (28,28)) 
                    image_resize = (255-image_resize)
                    #mostrar_imagem(image_resize)
                    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
                    text = pytesseract.image_to_string(image_resize,config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
                    #numeros = ['1','2','3','4','5','6','7','8','9']
                    #print(type(text))
                    try:
                        a = text.split()[0]
                        grid[i][j] = a
                        c += 1
                    except IndexError:
                        grid[i][j] = 0
                        d += 1
                        #text = int(text)
                        #print(text)
                        #grid[i][j] = int(text)
                        #print(grid)
                    

    grid =  grid.astype(int)
    #print(text)
    d = c + d
    #print(str(c) + " detetados /" + str(d) + " possiveis")
    #print(grid)
    return grid
    
main_ai()
