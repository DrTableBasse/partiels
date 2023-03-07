import json


class Materiel:
    def __init__(self, type, numero_serie):
        self.type = type
        self.numero_serie = numero_serie
class Clavier(Materiel):
    def __init__(self, type, numero_serie,nb_touches):
        super().__init__(type, numero_serie) #autocomplétion de vscode à m'expliquer si possible
        self.nb_touches = nb_touches
class Ecran(Materiel):
    def __init__(self, type, numero_serie,taille_ecran):
        super().__init__(type, numero_serie)
        self.taille_ecran = taille_ecran

class PC(Materiel):
    def __init__(self, type, numero_serie, ecran, clavier):
        super().__init__(type, numero_serie)
        self.ecran = ecran
        self.clavier = clavier
    
    def sauvegarder(self, nom_fichier):
        with open(nom_fichier, "w") as f:
            json.dump({
                "type": self.type,
                "numero_serie": self.numero_serie,
                "ecran": {
                    "type": self.ecran.type,
                    "numero_serie": self.ecran.numero_serie,
                    "taille_ecran": self.ecran.taille_ecran
                },
                "clavier": {
                    "type": self.clavier.type,
                    "numero_serie": self.clavier.numero_serie,
                    "nb_touches": self.clavier.nb_touches
                }
            }, f, indent=4)
    @classmethod
    def lire(cls, nom_fichier):
        with open(nom_fichier, "r") as f:
            contenu = json.load(f)
            return cls(
                contenu["type"],
                contenu["numero_serie"],
                Ecran(
                    contenu["ecran"]["type"],
                    contenu["ecran"]["numero_serie"],
                    contenu["ecran"]["taille_ecran"]
                ),
                Clavier(
                    contenu["clavier"]["type"],
                    contenu["clavier"]["numero_serie"],
                    contenu["clavier"]["nb_touches"]
                )
            )
        
def exercice3():
    # Création d'un clavier
    clavier = Clavier("Clavier AZERTY", "123456", 105)
    print("Type de clavier:", clavier.type)
    print("Numéro de série de clavier:", clavier.numero_serie)
    print("Nombre de touches de clavier:", clavier.nb_touches)
    print()
    
    # Création d'un écran
    ecran = Ecran("Ecran LCD", "789012", "24 pouces")
    print("Type d'écran:", ecran.type)
    print("Numéro de série d'écran:", ecran.numero_serie)
    print("Taille d'écran:", ecran.taille_ecran)
    print()
    
    # Création d'un PC avec l'écran et le clavier
    pc = PC("PC Portable", "345678", ecran, clavier)
    print("Type de PC:", pc.type)
    print("Numéro de série de PC:", pc.numero_serie)
    print("Type d'écran de PC:", pc.ecran.type)
    print("Numéro de série d'écran de PC:", pc.ecran.numero_serie)
    print("Taille d'écran de PC:", pc.ecran.taille_ecran)
    print("Type de clavier de PC:", pc.clavier.type)
    print("Numéro de série de clavier de PC:", pc.clavier.numero_serie)
    print("Nombre de touches de clavier de PC:", pc.clavier.nb_touches)
    print()
    
    # Sauvegarde du PC dans un fichier
    pc.sauvegarder("sauvegarde/mon_pc.json")
    print("PC sauvegardé dans le fichier 'sauvegarde/mon_pc.json'")
    
    # Lecture du PC sauvegardé depuis le fichier
    pc_sauvegarde = PC.lire("sauvegarde/mon_pc.json")
    print("Type de PC sauvegardé:", pc_sauvegarde.type)
    print("Numéro de série de PC sauvegardé:", pc_sauvegarde.numero_serie)
    print("Type d'écran de PC sauvegardé:", pc_sauvegarde.ecran.type)
    print("Numéro de série d'écran de PC sauvegardé:", pc_sauvegarde.ecran.numero_serie)
    print("Taille d'écran de PC sauvegardé:", pc_sauvegarde.ecran.taille_ecran)
    print("Type de clavier de PC sauvegardé:", pc_sauvegarde.clavier.type)
    print("Numéro de série de clavier de PC sauvegardé:", pc_sauvegarde.clavier.numero_serie)
    print("Nombre de touches de clavier de PC sauvegardé:", pc_sauvegarde.clavier.nb_touches)
    
exercice3()

            