nombre_d_entier = 3     # ce programme fonctionne pour un n-uplet avec n quelconque
                        # nombre_d_entier correspond à la taille du n-uplet
                        # l'affichage du résultat du test est  valable pour tout n
                        # par contre seul l'affichage d'un triplet est géré

import random
from random import randint

Bl ="\033[0;30m"
W = "\033[37m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
B = "\033[34m"
P = "\033[35m"
color = [W,R,G,O,B,P]

liste_nbr = []
coloration = []

for i in range(nombre_d_entier):          
    liste_nbr.append(randint(1,1000))       # formation du n-uplet à partir d'entiers tirés aléatoirement entre 1 et 1000
    coloration.append(random.choice(color)) # génération d'une coloration aléatoire du n-uplet
    
for i in range(nombre_d_entier):
    print(coloration[i],liste_nbr[i])


first_color = coloration[0]
monochr = True
i = 1
while monochr and i<nombre_d_entier:       # dés qu'un entier du n-uplet a une couleur différente du premier, le n-uplet n'est pas monochromatique     
    other_color = coloration[i]
    
    if first_color == other_color:
        monochr = True
    else:
        monochr = False
    i += 1

print(Bl,"Ce triplet (", end = "")
print(coloration[0],liste_nbr[0],",", end = "")
print(coloration[1],liste_nbr[1],",", end = "")
print(coloration[2],liste_nbr[2], end = "")

if monochr:
    print(Bl,") est monochromatique", end = "")
else:
    print(Bl,") n'est pas monochromatique", end = "")
    
