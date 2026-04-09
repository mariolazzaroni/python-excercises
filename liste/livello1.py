lista = []
lunghezza_lista = int(input("inserisci lunghezza lista: "))
i = 0
for i in range (0, lunghezza_lista):
    valore = int(input("Inserisci il valore da aggiungere alla lista: "))
    lista.append(valore)
print("la tua lista è: ", lista)
#sommo tutti gli elementi della lista
somma = 0
for valore in lista:
    somma += valore
print("la somma è:" ,somma)
#conto elementi > 5
j = 0
for valore in lista:
    if valore > 5:
        j+=1
print(j)
#trovo il massimo
massimo = lista[0]
for valore in lista:
    if valore > massimo:
        massimo = valore
print("Il massimo è:", massimo)
#stampa al contrario la lista
for i in range (0, len(lista)//2):
    lista[i], lista[len(lista)-1-i] = lista[len(lista)-1-i], lista[i]
print(lista)
