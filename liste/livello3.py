lista = []
lunghezza_lista = (int(input("Inserisci la lunghezza della lista: ")))
for i in range (lunghezza_lista):
    valore = int(input("Inserisci il valore della lista: "))
    lista.append(valore)
print("la tua lista è: ", lista)
#Rimuovi duplicati
lista_noduplicati = []
for valore in lista:
    if valore not in lista_noduplicati:
        lista_noduplicati.append(valore)
print("La lista senza duplicati è: ", lista_noduplicati)
#Trova il secondo massimo
massimo = lista[0]
for valore in lista:
    if valore > massimo:
        massimo = valore
massimo2 = lista[0]
for valore in lista:
    if valore > massimo2 and valore < massimo:
        massimo2 = valore
print("il secondo massimo della lista è: ", massimo2)
#inverti la lista (nuova lista)
lista_inversa = []
for i in range (len(lista)):
    lista_inversa.append(lista[len(lista)-1-i])
print(lista_inversa)
#se la lista è ordinata --> true, se la lista è disordinata --> false.
ordinata = True
for i in range (len(lista)-1):
    if lista[i] > lista[i+1]:
        ordinata = False
        break
print(ordinata)