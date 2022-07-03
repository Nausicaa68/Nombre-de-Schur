import time
start_time = time.time()

une_coloration_valide = True
coloration = []

n = 2   # car on calcul s(2)
N = 1
while une_coloration_valide == True:    # si il n'y a plus aucune coloration valide on s'arrête , coloration valide = aucun triplet monochromatique
    i=0
    coloration_non_valide = True
    while coloration_non_valide == True and i<n**N:   # dès qu'on trouve une coloration valide, on passe au N suivant
        liste_reste = []
        coloration = []
    
        if i == 0:            # génération d'une coloration par conversion de l'entier i en base 2
            for z in range(0,N):
                coloration.append(0)
        else:
            quotient = i
            while quotient != 0:
                reste = quotient % n
                quotient = quotient // n
                liste_reste.append(reste)
        
            for z in range(0,N-len(liste_reste)):    #compléter par des 0 pour avoir le bon nbr de bits
                liste_reste.append(0)
        
            for z in range(len(liste_reste)-1,-1,-1):
                coloration.append(liste_reste[z])    
        
        non_monochr = True
        
        a=1
        while non_monochr==True and a<N:   # formation des triplets (a,b,a+b)tant qu'on n'a pas trouvé de triplet monochromatique
            b=a
            while non_monochr==True and b<N:
                if (a+b)<=N:
              
                    #test de la validité de la coloration (une coloration est non valide dès l'existence d'un triplet monochromatique)
                    if non_monochr==True:
                        if coloration[a-1]==coloration[b-1] and coloration[b-1]==coloration[a+b-1]:  
                            non_monochr=False   
                b = b+1
            a = a+1
            
        if non_monochr==True:
           coloration_non_valide = False    #on a trouvé une coloration valide
        
        i = i+1
    print(N)
    if coloration_non_valide == True:    # il faut mettre une_coloration_valide à false quand il n'y a aucune coloration de valide
        une_coloration_valide = False
    else:
        N = N+1
               
print("Le nombre de Schur pour le n choisi vaut: ",N-1)

print("Temps d execution : %s secondes" % (time.time() - start_time))

