import time
start_time = time.time()

une_coloration_valide = True



n = 0
while n<2 or n>6:
    n = int(input("nbr de couleurs(max 6, min 2): "))    

liste_coloration_prec_valide = []
N = 1

for t in range(n):       # initialisation de la liste de colorations pur N=1
    coloration_ini=[]
    coloration_ini.append(t)
    liste_coloration_prec_valide.append(coloration_ini)
N=2
while une_coloration_valide == True:    # si il n'y a plus aucune coloration valide on s'arrête, coloration valide = aucun triplet monochromatique
  
    coloration_prec_valide = []
    liste_coloration_utile = []      # réinitialisation à chaque N
       
    for j in range(len(liste_coloration_prec_valide)):   
        coloration_prec_valide = liste_coloration_prec_valide[j] # on récupère chaque colorations valide à N-1
        equiv = 0
        for k in range(len(coloration_prec_valide)):   # on calcule le nombre décimal équivalent avec un bit supplémentaire  
            equiv += (coloration_prec_valide[k])*(n**(N-1-k)) 
        for l in range(0,n): # on stocke les n décimaux équivalents aux colorations utiles, c'est-à-dire à tester pour N
            liste_coloration_utile.append(equiv+l)
        
        
    liste_coloration_prec_valide = []       #réinitialisation après traitement de la précédente
    coloration_non_valide = True
    
    for i in range(len(liste_coloration_utile)):
                
        liste_reste = []
        coloration = []
        equiv_coloration = liste_coloration_utile[i]
    
        # génération de chaque coloration utile par conversion en base n du nombre décimal équivalent
        if equiv_coloration== 0:
            for z in range(0,N):
                coloration.append(0)
        else:
            quotient = equiv_coloration
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
        while non_monochr==True and a<=(N//2)+1:
            b=a
            while non_monochr==True and b<=N:
                if (a+b)<=N:
                    
                    #test de la validité de la coloration
                    if coloration[a-1]==coloration[b-1] and coloration[b-1]==coloration[a+b-1]:  
                        non_monochr=False   
                b = b+1
            a = a+1
            
        if non_monochr==True: #on a trouvé une coloration valide
            liste_coloration_prec_valide.append(coloration) # ajout de la coloration à la liste des colorations valides à traiter pour N+1
            coloration_non_valide = False    
        
            
    print(N)   
    if coloration_non_valide == True:    # il faut mettre une_coloration_valide à false quand il n'y a aucune coloration de valide
        une_coloration_valide = False
    else:
        N = N+1
                
print("Le nombre de Schur pour le n choisi vaut: ",N-1)

print("Temps d execution : %s secondes" % (time.time() - start_time))
