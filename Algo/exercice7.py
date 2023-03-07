def fonction():
    
    valeur = int(input("Veuillez choisir un nombre impair : "))
    addition_valeur_impair = 0
    
    for i in range(0, valeur):
        if i%2 ==1: #utilisation basique du module
            addition_valeur_impair = i + addition_valeur_impair

 
    print ("En additionnant tous les chiffres impair, on obtient ",addition_valeur_impair+valeur)

    
    
fonction()