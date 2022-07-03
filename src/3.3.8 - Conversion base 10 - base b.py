nbr_base10 = int(input("Saisir un nbr en base 10: "))   #conversion uniquement de nombres entiers positifs en base b
nbr_baseb = []    # liste des bits en base b, stockés dans le sens inverse 
sauvegarde = nbr_base10   # variable pour stocker le nbr entré par l'utilisateur pour l'affichage final

b = -1
while b<2:
    b = int(input("Choisissez votre base b (au moins 2): "))
    
while nbr_base10 != 0:
     
    nbr_baseb.append(nbr_base10 % b)
    nbr_base10 = nbr_base10 // b
    
chaine = ""    # stocke les bits du nbr en base b dans le bon sens d'affichage
if sauvegarde == 0:
    chaine = "0"

for i in range(len(nbr_baseb)-1,-1,-1):  #pas de -1, on parcourt nbr_baseb en sens inverse
    bit = nbr_baseb[i]
    if bit >= 10:           # à partir de 10, les bits correspondent aux caractères A, B, C, D.... 
        bit = chr(bit+55)   # pour obtenir le bon caractère, on utilise le code ASCII correspondant
    chaine += str(bit)   # on convertit notre variable bit, en une chaine de caractères pour l'ajouter à la variable chaine

print("Le nombre",sauvegarde,"en base",b,"donne:",chaine)