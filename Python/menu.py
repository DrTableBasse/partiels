##########################################

#mystère
import webbrowser


#ICI, permet juste d'éxécuter d'autre fichier.py
import subprocess


#Création d'un menu permettant d'exécuter d'autre programme python

def main_menu():

    print("Bienvenue au Menu Principal\n")
    print("Pour accéder à l'exercice 1, taper 1\n")
    print("Pour accéder à l'exercice 2, taper 2\n")
    print("Pour accéder à l'exercice 3, taper 3\n")
    print("Sinon taper 0 pour quitter le progarmme\n")


    choix = input("Entrer votre choix ici : ")

    if choix == "1" :
        subprocess.run(["python", "src/exercice1.py"])
    
    elif choix == "2":
        subprocess.run(["python", "src/exercice2.py"])
    elif choix == "3":
        subprocess.run(["python", "src/exercice3.py"])
    
    elif choix == "0":
        exit()
        
        
    
    else :
        print("Choix non valide. Veuillez réessayer")
        main_menu()

main_menu()