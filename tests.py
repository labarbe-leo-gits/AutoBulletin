# Script non-optimisé
# Version 'Console' 1.0
# Script commenté

# Script par LABARBE Léo,
# LPC Nicolas Ledoux

# ---------------------

# Import de librairies
from random import *

print("La génération customisée d'appréciation est en cours de développement. Pour le moment, tout relève du random pour des tests sans classifications.")

global F
F =  'Fille'
global G
G = 'Garçon'
PGT1 = {"Noham":G,"Laetitia":F, "Mohamed-Badache":G, "Imene":F, "Nihad":F, "Kenza":F, "Mouna":F,
"Mohamed-Bouhania":G, "Soraya":F, "Medina":F, "Okan":G, "Hamza":G, "Evane":G, "Kim":G,
"Rami":G, "Chaima":F, "Léo":G, "Xavier":G, "Nourhane":F, "Imane-Teriza":F,
"Seraphine":F, "Laura":F, "Wacil":G, "Sihame":F}
PGT2 = {}

# [NOM DU LYCEE]
# ... = {}

# Menu
print("Auto Complétion De Bulletin - Beta B-0-1")
print("Les réponses (hors exceptions) sont à présenter sous le format 'oui' et 'non' ; Pour les efforts, 'efforts'")

# Pronoms/grammaire/etc... en fonction du genre
masc = ["il", "sérieux", "un", "lui"]
fem = ["elle", "sérieuse", "une", "une"]

# Détecter le genre de l'individu via le dictionnaire PGT1
name = input("Nom de l'élève : ")
genre = PGT1.get(name)
print(f"Genre associé à {name} : {genre}")

# Afficher les variables suivant le genre
if genre == F :
    print(f"Pronoms : {fem}")
elif genre == G :
    print(f"Pronoms : {masc}")
else :
    print("Une erreur est survenue")

prono = 0

if genre == F :
    prono = fem
elif genre == G :
    prono = masc

# Définition globale des variables classifianty l'appréciation
# global talk
# global serious
# global results
# global participation
# global homework

# Définition de ces variables
talk = input("Bavardages (BCP, M, P, ABS) : ")
serious = input("Sérieux (y/n) : ")
results = input("Résultats (TS, S, CA, NA) : ")
participation = input("Participation (P, D, ABS) : ")
homework = input("Devoirs faits/rendus (y/n/sm) : ")

# Définition du message d'erreur 'type'
error = f"l'Entrée renseignée n'est pas valide. Merci de réessayer ultérieurement."

# APPRECIATIONS EN UNE SEULE LIGNE : IF STATEMENT VA CHERCHER DANS L'INDEX DU DICO
# Liste d'appréciations
# Déclaration globale de la variable
global appreciations
appreciations = [f"{name} est {prono[2]} élève {prono[1]} fournissant des résultats exemplaires tout comme son comportement en classe. Continue ainsi !",
                 f"{name} fait preuve de sérieux pendant les cours en s'appliquant avec soin. Je t'encourage à poursuivre ainsi !",
                 f"Un trimestre correcte pour {name} avec de bons résultats dans l'ensemble et un travail personnel sérieux. Bravo !",
                 f"Un trimestre peu qualitatif pour {name}. {prono[0]} a besoin de prendre plus confiance en {prono[3]} pour participer à l'oral.",
                 f"Un bon trimestre dans l'ensemble pour {name}. Cependant, il ne faut pas hésiter à prendre la parole en classe ou à poser des questions !",
                 f"Les notions sont en cours d'aquisition pour {name}. Afin de mieux réussir, il faut améliorer son travail personnel.",
                 f"Un trimestre noir pour {name}. Les résultats ne sont pas au rendez-vous creusant les lacunes ainsi qu'un travail personnel trop rare. Il faut vous ressaisir !",
                 f""]
appreciations_fin_annee = []
print(appreciations[6])

# Mise en global de variable 'int'. Ces integer définissent le niveau accordé par chaque critère. Par défaut 0.

# print(app_serious[0])
# Fonction de classification d'appréciations
def classing():
    global appreciations
    try :
        # Mettre à jour les listes dans des conditions bien spécifiques
        if talk and talk == 'ABS' :
            if serious and serious == 'y' :
                if results and results == 'TS':
                    if participation and participation == 'P':
                        if homework and homework == 'y':
                            print(appreciations[0])


    except Exception as e :
        print(e)    
            

classing()

classcount = int(input("Nombre d'élèves dans la classe : "))

# Boucle pour x élèves en classe
for i in range(classcount):
    # Nom de l'élève
    name = input("\nNom de l'élève : ")
    global istalking
    global isserious
    global isparticipating
    global isdoinghishomework
    # Dropdown conditions style bavardages etc ...
    istalking = input("Bavardages : ")
    isserious = input("Sérieux : ")
    isparticipating = input("Participe : ")
    studentresults = input("Bon résultats & efforts (oui, efforts) : ")
    isdoinghishomework = input("Travail rendu : ")
    # Check le genre de l'élève
    genre = PGT1.get(name)
    print(genre)
    # Définition du pronom il/elle & plus
    pron = ''
    adjective = ''
    if genre == F:
        pron = 'elle'
        adjective = 'une'
        print("Pronom défini en tant que 'ELLE' / Adjectif défini en tant que 'UNE'")
    elif genre == G:
        pron = 'il'
        adjective = 'un'
        print("Pronom défini en tant que 'IL' / Adjectif défini en tant que 'IL'")
    
    # print(pron)

    # Listes d'appréciations pré crées
    average_but_efforts = [
        f"{name} est {adjective} élève sérieux qui fournit des efforts constants malgré des résultats qui peuvent sembler moyens. Je l'encourage à continuer ainsi",
    f"Des résultats mitigés pour {name}. Malgré cela, {pron} fait de nombreux efforts montrant ainsi sa détermination. Continue ainsi !"
]
    print(choice(average_but_efforts))

    # Résumé bref
    print(f"\nRésumé :\nBavardages : {istalking}\nSérieux en classe : {isserious}\nParticipe au cours : {isparticipating}\nBons résultats & efforts : {studentresults}\nTravail rendu : {isdoinghishomework}")
    # Appréciation