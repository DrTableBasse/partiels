def fonction():
    tableau=[]
    message = input("Veuillez écrire une chaîne de caractère sur laquelle on va compter le nombre de majuscules / minuscules : ")
    majuscule = 0
    minuscule = 0
    #On regarde si chaque élément est en uppercase ou en lowercase
    for i in range(0,len(message)):
        tableau.append(message[i])
        if message[i].isupper() == True:
            majuscule = majuscule +1
        if message[i].islower() == True:
            minuscule = minuscule +1
    
    print("nombre de majuscules ",majuscule)
    
    print("nombre de minuscules ",minuscule)
    
fonction()