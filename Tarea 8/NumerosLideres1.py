lista = []
newlista = input("Ingrese los numeros separados por un espacio: ")
for i in newlista.split():
  es_lider = True
  for j in newlista.split()[newlista.split().index(i)+1:]:
    if int(i) <= int(j):
      es_lider = False
      break
  if es_lider:
    lista.append(i)
print(lista)
