def fonction():
    
    #attention, 1 n'est pas un chiffre pair.
    valeur = int(input("Veuillez choisir un nombre impair : "))
    
    tableau=[]
    
    
    for i in range(0, valeur+1):
        if i%2 ==0:
            valeur = i
            tableau.append(valeur)

 
    print(''.join(str(tableau)))

    
    
fonction()