nbr_base10 = int(input("Saisir un nbr en base 10: "))   #conversion uniquement de nombres entiers positifs en base 2
nbr_base2 = []    #liste des bits en base 2, stockés dans le sens inverse 
sauvegarde = nbr_base10   # variable pour stocker le nbr entré par l'utilisateur pour l'affichage final
   
while nbr_base10 != 0:
     
    nbr_base2.append(nbr_base10 % 2)
    nbr_base10 = nbr_base10 // 2

chaine = ""    # stocke les bits du nbr en base 2 dans le bon sens d'affichage
if sauvegarde == 0:
    chaine ="0"
    
for i in range(len(nbr_base2)-1,-1,-1):  #pas de -1, on parcourt nbr_base2 en sens inverse
    chaine += str(nbr_base2[i])   # on convertit les bits de nbr_base2,entiers, en une chaine de caractères pour l'ajouter à la variable chaine

print("Le nombre",sauvegarde,"en base 2 donne:",chaine)
