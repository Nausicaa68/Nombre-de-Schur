N = 50

R = "\033[31m"
B = "\033[34m"

for i in range(1,N+1):
    if i%2 == 0:          #on teste si l'entier i est pair
        print(R,i,end = "")
    else:
        print(B,i,end = "")
