# se importan las librerías sys y os para poder cambiar el 
# path a la raiz de las carpetas a, b y c, es decir 'imports'

import sys, os
ruta=__file__
# al ser una ruta a un archivo en una carpeta de segundo nivel, 
# es necesario hacer tres saltos de directorio para llegar 
# al directorio raiz
ruta = os.path.dirname(ruta)
ruta = os.path.dirname(ruta)  
ruta = os.path.dirname(ruta)  
sys.path.append(ruta)
print(ruta)
print("------------------------")

import a.x as funx
import b.y as funy


def f1z ():
    print("Esta es la función f1z")
    funy.f1y()

def f2z ():
    print("Esta es la función f2z")
    funx.f2x()

z1 = 10

z2 = 30


if __name__ == "__main__":
    print("Llamando a la función f2z....")
    f2z()

    print("Llamando a la función f1z....")
    f1z()