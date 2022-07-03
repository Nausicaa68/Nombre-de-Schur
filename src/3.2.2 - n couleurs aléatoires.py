from random import randint
import random

W = "\033[37m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
B = "\033[34m"
P = "\033[35m"

color = [W,R,G,O,B,P]
my_color = []
nb_color_used = randint(1,6)    #nbr de couleurs tiré aléatoirement

for i in range(nb_color_used):  
    alea_color = randint(0,len(color)-1)
    my_color.append(color[alea_color])
    color.remove(color[alea_color])



N = 0    
while N<6:
    N = int(input("nbr d'entiers à colorer (au moins 6): "))     # on doit prendre N au moins égal à 6 pour éviter d'avoir une boucle infinie si N < nb_color_used

color_unused = [R]                 # pour entrer dans la boucle au moins 1 fois
while len(color_unused)!=0:        #tant que toutes les couleurs de my_color ne sont pas utilisées
    
    color_unused = []       #copie des couleurs à utiliser dans color_unused
    for k in range(0,len(my_color)):
        color_unused.append(my_color[k])

    coloration = []
    for n in range(N):                #génération d'une coloration aléatoire des N premiers nombres entiers
        choix_random = random.choice(my_color)
        coloration.append(choix_random)
        if choix_random in color_unused:
            color_unused.remove(choix_random)     # on enlève de color_unused les couleurs déjà utilisées, pour s'assurer que toutes sont présentes

print("nbr de couleurs a utiliser:",nb_color_used)

for m in range(0,N):              # Affichage des N premiers nombres entiers à partir de coloration
    print(coloration[m],m+1,end = "")

