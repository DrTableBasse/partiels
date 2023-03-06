def fonction():
    
    message = input("Veuillez rentrer la phrase à laquelle vous voulez savoir le nombre de mots : ")
    tableau = []
    nb_espace = 0
    for j in range(0, len(message)):
        tableau.append(message[j])
        
    for i in range(0,len(tableau)):
       if tableau[i].isspace() == True :
           nb_espace = nb_espace+1
           
    print("Il y a ", nb_espace, "d'espace dans votre chaîne.")
    
    
    
fonction()