def fonction():
    print("\nDisclaimer : Ici on ne prendra que les caractères n'étant pas dans la table ASCII\n")

    tableau=[]
    message = input("Veuillez écrire une chaîne de caractère sur laquelle on va compter le nombre de majuscules / minuscules : ")
    tableau_ascii=[]

    for i in range(0,len(message)):
        tableau.append(message[i])
        #isascii renvoie un booléen si le caractère qu'on lui propose est dans la table ASCII ou non
        if tableau[i].isascii()==True:
            tableau_ascii.append(tableau[i])
    print(tableau_ascii)
    
    
    
fonction()