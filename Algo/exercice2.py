def ordre():
    message = input("Choisir une chaîne de caractère pour vérifier qu'elle est dans l'ordre alphabétique ou non : ")
    message_ordre = []
    for i in range(0, len(message)):
        message_ordre.append(message[i])
        tableau_ordre = message_ordre 
        message_ordre.sort()
    
    if tableau_ordre != message_ordre:
        print("La liste n'est pas dans l'ordre alphabétique.")
    else :
        print("La liste est dans l'ordre alphabétique.")
    
    
    
    
    
    
ordre()