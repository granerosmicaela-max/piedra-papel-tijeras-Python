nombre1 = input("¿Cómo se llamará el jugador 1: " )
nombre2 = input("¿Cómo se llamará el jugador 2: ")

jugador1 = input(nombre1 + " ¿Qué eliges? ¿Piedra,papel o tijera?: ")
jugador2 = input(nombre2+" ¿Qué eliges? ¿Piedra,papel o tijera?: ")

if(jugador1.lower()==jugador2.lower()):
    print("¡Ha sido un empate!")
elif(jugador1.lower()== "Piedra"and jugador2.lower()== "tijera")or(jugador1.lower()== "papel" and jugador2.lower() == "Piedra") or(jugador1.lower()== "Tijera" and jugador2.lower()== "papel"):
    print ("Ha ganado:",nombre1)
else:
    print("Ha ganado:",nombre2)
