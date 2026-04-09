lista = []
lunghezza_lista = (int(input("Inserisci lunghezza lista: ")))
for i in range (0, lunghezza_lista):
    valore_lista = int(input("Valore della lista: "))
    lista.append(valore_lista)
print(lista)
#quante volte compare un numero?
numero_da_contare = int(input("Inserisci il valore che vuoi contare: "))
i = 0
for valore in lista:
    if valore == numero_da_contare:
        i+=1
print("Il numero ", numero_da_contare, " compare ", i, " volte")
#Restituisci l'indice di 9 
i = 0 
while i < len(lista):
    if lista[i] == 9:
        print("L'indice del valore 9 è: ", i)
    i += 1
#Crea una nuova lista filtrata con solo numeri pari
lista_pari = []
for valori in lista:
    if valori % 2 == 0: 
        lista_pari.append(valori)
print(lista_pari)
#Somma solo i numeri pari
somma_pari = 0
for valore in lista:
    if valore % 2 == 0:
        somma_pari += valore
print("La somma dei numeri pari è: ", somma_pari)