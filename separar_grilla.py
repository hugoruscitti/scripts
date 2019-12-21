#!/usr/local/bin/python3

import sys
import os
from PIL import Image

if len(sys.argv) != 4:
    print("Número incorrecto de parámetros")
    print("")
    print("El uso correcto requiere estos argumentos:")
    print("")
    print("  python3 separar_grilla.py archivo.png filas columnas")
    print("")
    print("Por ejemplo:")
    print("")
    print("  python3 separar_grilla.py fixtures/explosion.png 1 7")
    print("")
    sys.exit(1)

ARCHIVO = sys.argv[1]
FILAS = int(sys.argv[2])
COLUMNAS = int(sys.argv[3])

im = Image.open(ARCHIVO)
nombre = os.path.splitext(os.path.basename(ARCHIVO))[0]

width = im.width
height = im.height

cuadro_ancho = width / COLUMNAS
cuadro_alto = height / FILAS


for f in range(FILAS):
    for c in range(COLUMNAS):
        izquierda = c*cuadro_ancho
        arriba = f*cuadro_alto
        derecha = izquierda + cuadro_ancho
        abajo = arriba + cuadro_alto
        tile = (izquierda, arriba, derecha, abajo)
        nim = im.crop(tile)

        indice = f * COLUMNAS + c
        nim.save(f"{nombre}_{indice}.png")
