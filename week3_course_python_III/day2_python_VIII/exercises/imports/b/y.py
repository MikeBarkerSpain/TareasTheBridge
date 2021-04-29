
# se importan las librerías sys y os para poder cambiar el 
# path a la raiz de las carpetas a, b y c, es decir 'imports'

import sys, os
ruta=__file__
# al ser una ruta a un archivo en una carpeta de primer nivel, 
# es necesario hacer dos saltos de directorio para llegar 
# al directorio raiz
ruta = os.path.dirname(ruta)
ruta = os.path.dirname(ruta)
# print (ruta)
sys.path.append(ruta)
# print(sys.path)
print("-------------")
#print(ruta)

""" CUANDO SE IMPORTA UN ARCHIVO; SE EJECUTA TODO EL ARCHIVO"""
import a.x as funx

def f1y ():
    print("Esta es la función f1y")
    funx.f1x()

def f2y ():
    print("Esta es la función f2y")
    funx.f2x()

y1 = 7

y2 = 20

if __name__ == "__main__":
    print("Llamando a la función f1y...")
    f1y()
    print("Llamando a la función f2y...")
    f2y()