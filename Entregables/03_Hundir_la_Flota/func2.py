def insert_boat_check(pos_str, boat_len, Tablero):

    # lo primero es comprobar si el formato de insercion es el correcto
    # los dos puntos son un elemento constante en la inserción de posición
    if pos_str.count(':')==1:

        # comprobación de elementos de una inserción vertical 
        if pos_str.count("v")==1:   # Debe haber una única letra de orientación
            if pos_str.count ("h") == 0:    # no puede ser horizontal
                ori = "v"
            else:
                print("Position format error for this boat, type it again.")
                return False

        # comprobación de elementos de una inserción horizontal 
        elif pos_str.count("h")==1: # Debe haber una única letra de orientación
            if pos_str.count ("v") == 0:    # no puede ser vertical
                ori = "h"
            else:
                print("Position format error for this boat, type it again.")
                return False
        else:
            print("Position format error for this boat, type it again.")
            return False
    else:
        print("Position format error for this boat, type it again.")
        return False
        
    # A continuación se descompone el string para obtener los números
    try:
        list1 = pos_str.split(ori)
        list2 = list1[-1].split(":")
        num1 = int(list1[0])
        num2 = int(list2[0])
        num3 = int(list2[1])
        
        # Se comprueban la coherencia de las coordenadas
        coord_OK = False
        if (num1 >= 1 and num1 <= 10) and  (num2 >= 1 and num2 <= 10) and (num3 >= 1 and num3 <= 10):
            coord_OK = True

        # Se comprueba que el largo del barco y las coordenadas coinciden
        len_coord_OK = False
        if num3-num2+1 == boat_len:
            len_coord_OK = True
        # Si no hay error de formato y la función prosigue, se devuelve una lista con la orientación y las coordenadas del barco
        if coord_OK:
            if len_coord_OK:
                list_posi = [ori, num1, num2, num3]
            else:
                print ("Coordenates do not match with the boat lenght, type it again.") 
                return False   
        else:
            print("A coordenate is out of range, type it again.")
            return False
    except ValueError:
        print("Position format error for this boat, type it again.")
        return False

    # Por último, se comprueban las posiciones ya ocupadas del tablero
    if list_posi[0] == 'h':
        for i in range(list_posi[2]-1, list_posi[3]):
            if Tablero[list_posi[1]-1][i] == '~':
                Tablero[list_posi[1]-1][i] = '#'
            else:
                print("One of the positions of the boat is already taken.")
                return False
        return True
    else: 
        for i in range(list_posi[2]-1, list_posi[3]):
            if Tablero[i][list_posi[1]-1] == '~':
                Tablero[i][list_posi[1]-1] = '#'
            else:
                print("One of the positions of the boat is alreaady taken.")
                return False
        return True

    return list_posi

   


# Esta función recibe una lista con los elementos de la posición de un barco 
# y modifica el tablero de juego para dibujarlo
def print_board (Tablero):
    print("------------------------------------------")
    for i in range(0,10):
        print (Tablero[i])
    print("------------------------------------------")
    