lista=[]
newlista=input("Ingrese los numeros separados por un espacio: ")
for valor in newlista.split():
    if valor not in lista: 
        lista.append(valor)
print(lista)