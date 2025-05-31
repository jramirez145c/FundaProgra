n = int(input("Ingresa un número: "))
print("Proceso de reducción para ", n, ": ")
while n >= 10:
    print(n, end=" = ")
    suma = 0
    for i in str(n):
        suma += int(i)
    print(suma)
    n = suma

print("El resultado final es: ", n)