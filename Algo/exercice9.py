def fonction():
    
    valeur = input("Veuillez choisir un nombre pour savoir si il est un palindrome : ")
    tableau = []
    for i in range(0, len(valeur)):
        tableau.append(valeur[i])
        
    for j in range(0, len(valeur)):
        #On check la valeur précédente avec celle actuelle
        if tableau[j-1] != tableau[j]:
            print("False")
            break
        else :
            print("True")
            break
    
    
    
    
fonction()