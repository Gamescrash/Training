# BASE PYTHON (only for to remember something)

#math ex
    # import math

    # print(math.pi)

#file
    # f=open("./testo.txt","a")
    # # f.write("\nThis is a test n3")
    # print(f.read())
    # f.close()

n = [1, 2, 3, 4, 5, 6]

somma_totale = 0  # Variabile per accumulare la somma

# Sommare le estremità
for i in range(len(n) // 2):
    somma = n[i] + n[-(i + 1)]  # Somma delle estremità
    somma_totale += somma       # Aggiungi alla somma totale

print(f"Somma totale delle estremità: {somma_totale}")
