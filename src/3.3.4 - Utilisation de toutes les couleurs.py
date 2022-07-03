from random import randint
import random
Bl = "\033[30m"
W = "\033[37m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
B = "\033[34m"
P = "\033[35m"

color = [W,R,G,O,B,P]
my_color = []

for i in range(randint(1,6)):   #nbr de couleurs tiré aléatoirement
    alea_color = randint(0,len(color)-1)
    my_color.append(color[alea_color])
    color.remove(color[alea_color])

print("nbr de couleurs à utiliser:",len(my_color))

color_unused = []    #copie des couleurs à utiliser dans color_unused
for k in range(0,len(my_color)):
    color_unused.append(my_color[k])
   
  
N = int(input("nbr d'entiers à colorer : "))     

coloration = []

for n in range(N):      #génération d'une coloration aléatoire des N premiers nombres entiers
    choix_random = random.choice(my_color)
    coloration.append(choix_random)
    if choix_random in color_unused:
        color_unused.remove(choix_random)    # on enlève de color_unused les couleurs déjà utilisées

for m in range(0,N):
    print(coloration[m],m+1,end = "")

if len(color_unused)!=0:    # toutes les couleurs n'ont pas été utilisées
    print(Bl,"\nLa coloration utilise toutes les couleurs : FAUX")
else:
    print(Bl,"\nLa coloration utilise toutes les couleurs : VRAI")