n = int(input("Nombre de couleur n : "))
N = int(input("Nombre d'entiers à colorier : "))

Bl = "\033[30m"
W = "\033[37m"
R = "\033[31m"
G = "\033[32m"
O = "\033[33m"
B = "\033[34m"
P = "\033[35m"

color = [W,R,G,O,B,P]
liste_colorations =[]

for i in range (0, n**N):     # génération de la liste des colorations
    liste_reste = []               #la liste des restes correspond  à la liste des bits du nombre en base n stockés dans le sens inverse
    liste_bits_bonordre = []
    
    if i == 0:
        for z in range(0,N):
            liste_bits_bonordre.append(0)
    else:
        quotient = i
        while quotient != 0:
            reste = quotient % n
            quotient = quotient // n
            liste_reste.append(reste)
        
        for z in range(0,N-len(liste_reste)):    #compléter par des 0 pour avoir le bon nbr de bits
            liste_reste.append(0)
        
        for z in range(len(liste_reste)-1,-1,-1):      #on inverse liste_reste pour avoir la liste des bits dans le bon ordre
            liste_bits_bonordre.append(liste_reste[z])
            
    liste_colorations.append(liste_bits_bonordre)        # liste_bits_bonordre correspond à une coloration

for j in range (0, n**N):    # affichage de la liste des colorations
      
    print(Bl,"\nColoration n°",j+1,": ", end = "")
    for k in range (0,N):
        print(color[liste_colorations[j][k]],k+1, end = "")