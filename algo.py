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
masc = ["il", "sérieux"]
fem = ["elle", "sérieuse"]

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
# Dictionnaires d'appréciations
#app_results = {f"Des résultats qui ne sont malheureusement pas à la hauteur. Toutefois l'attitude de {eleve} est {attitude}"}
app_talk = {}
app_participe = {}
app_homework = {}
app_serious = [f"{name} ne fait preuve d'aucun sérieux dans les travaux entrepris en classe. Il faut se resaisir !"]

appreciations = []

# Mise en global de variable 'int'. Ces integer définissent le niveau accordé par chaque critère. Par défaut 0.
global serious_lvl, results_lvl, talk_lvl, participation_lvl, homework_lvl
serious_lvl = 0
results_lvl = 0
talk_lvl = 0
participation_lvl = 0
homework_lvl = 0

# print(app_serious[0])
# Fonction de classification d'appréciations
def classing():
    global serious_lvl, results_lvl, talk_lvl, participation_lvl, homework_lvl
    try :
        if serious :
            if serious == 'y':
                serious_lvl = 1
            elif serious == 'n':
                serious_lvl = 2     
                
        if results :
            if results == 'TS':
                results_lvl = 1
            elif results == 'S':
                results_lvl = 2
            elif results == 'CA':
                results_lvl = 3
            elif results == 'NA':
                results_lvl = 4   
                
        if talk :
            if talk == 'BCP':
                talk_lvl = 4
            elif talk == 'M':
                talk_lvl = 3
            elif talk == 'P':
                talk_lvl = 2
            elif talk == 'ABS':
                talk_lvl = 1           
                
        if participation :
            if participation == 'P':
                participation_lvl = 1
            elif participation == 'D':
                participation_lvl = 2
            elif participation == 'ABS':
                participation_lvl = 3
                      
        if homework :
            if homework == 'y':
                homework_lvl = 1
            elif homework == 'n':
                homework_lvl = 3
            elif homework == 'sm':
                homework_lvl = 2

        if serious and serious_lvl == 1 :
            print("eleves serieux")


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