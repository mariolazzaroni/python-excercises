lista = [3, 7, 2, 9]
print(lista[0])
print(lista[3])
i = 0
for i in range (0, len(lista)):
    print(lista[i])
    i+=1
for indice, valore in enumerate(lista):
    print(indice, valore)
valore_da_aggiungere = int(input("inserisci valore da aggiungere alla lista: "))
lista.append(valore_da_aggiungere)
print(lista)
a = 1
lista.pop(a)
print(lista)
b = 2
if b in lista:
    lista.remove(b)
    print(lista)