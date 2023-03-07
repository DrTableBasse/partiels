def seuil(P,T):
    N = 0
    print("|    P    |    N    |")
    while P < 1000:
        
        P = P * T
        if P > 1000:
            break
        N = N+1
        
        print("|  ",round(P,2),"|     ",round(N,2),"|")
    
    return N



def exercice1():
    N = 0
    P = float(input("Veuillez choisir le prix d'un article : "))
    T = float(input("Veuillez choisir le taux d'inflation : "))
    
    N = seuil(P,T)
    print("Nmax : ",N)
    
    
    
    
    
    




exercice1()