def seuil(P,T):
    N = 0
    print("|    P       |    N     |")
    print("|------------|----------|")
    while P < 1000:
        
        P = P * T
        if P > 1000:
            break
        N = N+1
        
        print("|  {:<8.2f}  |  {:<6}  |".format(P, N))
    
    return N



def exercice1():
    N = 0
    P = float(input("Veuillez choisir le prix d'un article : "))
    T = float(input("Veuillez choisir le taux d'inflation : "))
    
    N = seuil(P,T)
    print("Nmax : ",N)
    
    
    
    
    
    




exercice1()