n = 0
while n < 6:
    n = int(input("Rentrer le nombre de couleur n : "))

borne1 = ((3**n)-1)/2
borne2 = 1

for i in range(1,n+1):
    borne2 *= i
borne2 = (3*borne2) - 1

print("Le nombre de Schur S(",n,") est compris dans l'intervalle [%.2e"%borne1,";","%.2e"%borne2,"]")      #on formatte la borne 2 en écriture scientifique et on se limite à 2 chifres après la virgule