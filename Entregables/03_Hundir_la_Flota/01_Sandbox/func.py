import numpy as np 
from re import split
import json

# Esta función recibe una lista con los elementos de la posición de un barco 
# y modifica el tablero de juego para dibujarlo
def print_board (Tablero):
    print("-----------TABLERO PROPIO-------------------")
    tableroNP = np.array(Tablero)
    print(tableroNP)
    print("--------------------------------------------")

def print_board_enemy (Tablero):
    print("-----------TABLERO ENEMIGO------------------")
    tableroNP = np.array(Tablero)
    tableroShade = np.where(tableroNP == '#', '~', tableroNP)
    print(tableroShade)          
    print("--------------------------------------------")   

def launch_torpedo(board):
    #player_name = "First_player ->"+ input("Enter your name: ")
    coord = input("Enter coordinates (row x column): ")

    # Restamos 1 a las coordinadas porque el jugador asume que el tablero empieza en la posición 1 y no 0
    coord = split("\D+", coord)
    coord_x = int(coord[0]) - 1
    coord_y = int(coord[1]) - 1

    # Comprobamos si el jugador ha dado a algun barco
    if board[coord_x][coord_y] == "#":
        print("You have hit me!")
        board[coord_x][coord_y] = "X"
        #print(board)
    # Comprobamos si el jugador introduce una posición ya mencionada antes
    elif board[coord_x][coord_y] == "X" or board[coord_x][coord_y] == "o":
        print("You have already said that position before. Try another")
    
    # Comprobamos si el jugador ha fallado
    else:
        print("Water! maybe next time")
        board[coord_x][coord_y] = "o"
        #print(board)
    # Comprobamos si ya no quedan mas barcos
    if "#" not in np.array(board):
        print("You have destroyed my fleet, you win!")
        return False
    else:
        return True  

def guardado_auto (name_J1,Tablero_J1, Flota_J1,name_J2,Tablero_J2, Flota_J2, turno):
    # Se guarda el avance de la partida en la carpeta del histórico
    nombre_archivo = f"HundirFlota_T{turno}.json"
    mi_diccionario = {"Name_J1": name_J1, 
                    "Flota_J1": Flota_J1, 
                    "Tablero_J1":Tablero_J1,
                    "Name_J2": name_J2, 
                    "Flota_J2": Flota_J2, 
                    "Tablero_J2":Tablero_J2,
                    "Turno":turno}
    with open(nombre_archivo, 'w+') as outfile:
        json.dump(mi_diccionario, outfile, indent=4)