def suite(A, B, N):
    U0 = A
    U1 = B
    list = {0:u0, 1:u1}
    n=0
    Un = U1
    #erreur dans la suite
    #Il y a Un-1 qui est définit mais à aucun moment on ne peut trouver Un-1 et ça ne colle pas avec les résultats donnés.
    #A revérifier
    
    while n!=N:
        u0 = (u0+u1)/2
        u1 = 2 / (1/u0 +1/u1)
        n = n+1
        list[n] = u0
    return list
    

    
def exercice2():
    
    try :
       A = int(input("Veuillez choisir la valeur de A : "))
    except ValueError:
       print("Veuillez choisir un entier naturel.")
    
    try :
       B = int(input("Veuillez choisir la valeur de A : "))
    except ValueError:
       print("Veuillez choisir un entier naturel.")
    try:    
        N = int(input("Veuillez choisir la valeur de N : "))
    except ValueError:
       print("Veuillez choisir un entier naturel.")
    list = suite(A,B,N)
    
    print(list)
    
    
exercice2()