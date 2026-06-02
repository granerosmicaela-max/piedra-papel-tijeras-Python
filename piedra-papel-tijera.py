nombre1 = input("¿Cómo se llamará el jugador 1: " )
nombre2 = input("¿Cómo se llamará el jugador 2: ")

jugador1 = input("Hola ¿Qué eliges? ¿Piedra,papel o tijera?: ")
jugador2 = input("Hola jugador 2 ¿Qué eliges? ¿Piedra,papel o tijera?: ")

if(jugador1==jugador2):
    print("¡Ha sido un empate!")
elif(jugador1== "Piedra"and jugador2== "tijera")or(jugador1== "papel" and jugador2 == "Piedra") or(jugador1== "Tijera" and jugador2== "papel"):
    print ("Ha ganado:",nombre1)
else:
    print("Ha ganado:",nombre2)
