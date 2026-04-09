lista = []
lunghezza_lista = int(input())
for i in range (lunghezza_lista):
    valore_lista = int(input())
    lista.append(valore_lista)
#ordiniamo la lista
for j in range(len(lista)-1):
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
print(lista)