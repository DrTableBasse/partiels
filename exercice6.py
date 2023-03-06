def fonction():
    
    tableau = [] 
    nv_tableau=[]
    message = input("Veuillez écrire une chaîne de caractère sur laquelle on va compter le nombre de majuscules / minuscules : ")
    nb_lettre = int(input("Veuillez choisir le nombre de lettre que l'on va répéter \n Exemple Hi,3 --> HHHiii  :"))
    
    #Ici on va imbriquer deux boucle pour :
    # 1) ajouter à un tableau chaque caractères dans un index.
    # 2) on boucle une deuxième fois pour ajouter x fois chaque caractères.
    for i in range(0,len(message)):
        tableau.append(message[i])
        for j in range(0, nb_lettre):
            nv_tableau.append(tableau[i])
            
    print(''.join(nv_tableau))
    
    
    
fonction()