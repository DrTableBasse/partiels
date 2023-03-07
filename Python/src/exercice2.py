def suite(A, B, N):
    U0 = A
    U1 = B
    Un_1 = U0
    Un = U1
    for n in range(2, N+1):
        Un = (Un + Un_1) / 2
        Un_1 = 2 / ((1/Un_1) + (1/Un))
    return (Un, Un_1)
    

    
def exercice2():
    
    A = int(input("Veuillez choisir la valeur de A : "))
    B = int(input("Veuillez choisir la valeur de B : "))
    N = int(input("Veuillez choisir la valeur de N : "))
    resultat = suite(A,B,N)
    
    print(resultat)
    
    
exercice2()