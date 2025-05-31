import random
num = random.randint(1,100)
adivinar=0
while adivinar!=num:
    adivinar=int(input("Ingrese un numero entre 1 y 100: "))
    if adivinar>num:
        print("El numero secreto es menor")
    elif adivinar<num:
        print("El numero secreto es mayor")
    elif adivinar==num:
        print("Felicidades! Has adivinado el numero secreto")

