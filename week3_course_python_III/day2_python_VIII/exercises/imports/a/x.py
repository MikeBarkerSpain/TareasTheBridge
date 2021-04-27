# se importan las librerías sys y os para poder cambiar el 
# path a la raiz de las carpetas a, b y c, es decir 'imports'

import sys, os
ruta = __file__
# al ser una ruta a un archivo en una carpeta de primer nivel, 
# es necesario hacer dos saltos de directorio para llegar 
# al directorio raiz
ruta = os.path.dirname(ruta)
ruta = os.path.dirname(ruta)
print("-------------")
print (ruta)

import c.z as funcz

def f1x ():
    print("Esta es la función f1x")

def f2x ():
    print("Esta es la función f2x")
    funcz.f2z()

x1 = 4

x2 = 3

# el código a partir de aquí no se ejecuta (incluso en importaciones)
if __name__ == "__main__":      
    print("Llamando a la función f1x...")
    f1x()