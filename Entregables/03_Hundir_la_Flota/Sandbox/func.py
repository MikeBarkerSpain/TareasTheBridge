import numpy as np 

# Esta función recibe una lista con los elementos de la posición de un barco 
# y modifica el tablero de juego para dibujarlo
def print_board (Tablero):
    print("------------------------------------------")
    for i in range(0,10):
        print (Tablero[i])
    print("------------------------------------------")

def print_board_enemy (Tablero):
    print("------------------------------------------")
    tableroNP = np.array(Tablero)
    tableroShade = np.where(tableroNP == '#', '~', tableroNP)
    print(tableroShade)          
    print("------------------------------------------")    