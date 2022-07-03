liste_triplets=[]     # la liste de tous les triplets
triplet=[]            # un triplet(a,b,a+b)

p = 101
while p > 100 or p<0:
    p = int(input("Choisir un entier positif p inférieur ou égal à 100: "))

for a in range(1,p+1):         # pour a de 1 à l'entier p choisi
    for b in range(a,p+1):     # on commence à a pour ne pas traiter les triplets où a>b
        if (a+b)<=p:
            triplet = []
            triplet.append(a)
            triplet.append(b)
            triplet.append(a+b)
            liste_triplets.append(triplet)

print("Pour p =",p,"La liste de tous les triplets de type (a, b, a+b) est:\n",liste_triplets)