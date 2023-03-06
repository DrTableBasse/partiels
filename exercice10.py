def fonction():
    
    tableau1=[]
    tableau2=[]
    compteur = 0
    print("Consigne : Entrer deux chaîne de caractères identiques en taille.\n")
    valeur1= input("Veuillez choisir une première chaîne de caractères  : ")
    valeur2= input("Veuillez choisir la seconde chaîne de caractères à comparer : ")
    
    
    #On met les caractères de chaque chaîne dans un tableau qu'on va ensuite comparer.
    for i in range(0,len(valeur1)):
        tableau1.append(valeur1[i])
    for j in range(0,len(valeur2)):
        tableau2.append(valeur2[i])
    
    
    for x in range(0, len(valeur1)):
        
        if tableau1[x] not in tableau2[x]:
            compteur = compteur + 1
    #Pour une raison que j'ignore, il s'incrémente une fois de plus alors que je ne rentre pas dans la boucle.
    print(compteur-1)
fonction()