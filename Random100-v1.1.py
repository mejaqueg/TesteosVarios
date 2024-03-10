# Elegir un número del 1 al 100, si la máquina elige uno mayor gana.
# Este juego aún contiene errores.
# v1.1:
# Si se escribe una letra en vez de un número, el juego colapsa.

import random
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+                Bienvenido a este minijuego.             +")
print("+          Tendrás que elegir un número aleatorio.        +")
print("+  Si yo elijo uno mayor gano, de lo contrario tú ganas.  +")
print("+            Para salir solo escribe: salir               +")
print("+                          ¿Listo?                        +")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")


def elegir():
    numero = ""
    while numero != "salir":
        numero = input("Escribe un número del 1 al 100: ")
        if numero.lower() == "salir":
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+                 ¡Gracias por jugar!                     +")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
            return
        else:
            numero_aleatorio = random.randint(1, 100)
            numero = int(numero)
            print("La máquina eligió el número: " + str(numero_aleatorio))
        if numero_aleatorio > numero:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+                  Gano la máquina :c                     +")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
        if numero_aleatorio < numero:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+                      Ganaste! :D                        +")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")
        if numero_aleatorio == numero:
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("+                 ¡Wow! Es un empate D:                   +")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("")


elegir()
