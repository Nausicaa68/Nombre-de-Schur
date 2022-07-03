from random import randint
import random
R = "\033[31m"
B = "\033[34m"
Bl = "\033[30m"

my_color = [R,B]
color_unused = [R,B]
coloration = []


entier_max = randint(2,20)    # N, nbr d'entiers à colorier
print("N = ",entier_max)
  
   
while len(color_unused)!=0:     # on génère une coloration en s'assurant d'avoir toutes les couleurs utilisées
    color_unused = [R,B]
    coloration = []
    for i in range(entier_max):
        choix_random = random.choice(my_color)
        coloration.append(choix_random)
        if choix_random in color_unused:
            color_unused.remove(choix_random)


print("La coloration:", end = "")
for i in range(0,entier_max):
    print(coloration[i],i+1, end = "")


liste_triplets=[]     # la liste de tous les triplets
triplet=[]        # le triplet(a,b,a+b)
non_monochr=True

for a in range(1,entier_max+1):         # génération des triplets (a, b, a+b) selon la méthode de l'exercice 3.3.2
    for b in range(a,entier_max+1):     # on génère tous les triplets pour l'affichage
        if (a+b)<=entier_max:
            triplet = []
            triplet.append(a)
            triplet.append(b)
            triplet.append(a+b)
            liste_triplets.append(triplet)
            if non_monochr==True:       # si on a déjà trouvé un triplet monochromatique, il est inutile de tester les suivants
                if coloration[a-1]==coloration[b-1] and coloration[b-1]==coloration[a+b-1]:    #si on rencontre un triplet monochromatique le programme affichera FAUX
                    non_monochr=False                                                          

print(Bl,"\nLa liste de tous les triplets est:")


for i in range(len(liste_triplets)):
    triplet = liste_triplets[i]
    print(Bl,"(", end = "")
    print(coloration[triplet[0]-1],triplet[0],",", end = "")
    print(coloration[triplet[1]-1],triplet[1],",", end = "")
    print(coloration[triplet[2]-1],triplet[2], end = "")
    print(Bl,")", end = "")

print("\n",non_monochr,": tous les triplets ne sont pas monochromatiques.")
    