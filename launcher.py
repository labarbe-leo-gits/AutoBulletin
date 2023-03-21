# Ce script lance l'application
# Il a pour but d'alléger le lancement

try :

    # Import de librairies & de scripts locaux
    from tkinter import messagebox
    import logging
    import AdditionalScripts.GUI.new_gui as gui
    import AdditionalScripts.HiddenData.logs_config as logs_config
    import msvcrt as m

# En cas d'erreur
except Exception as e :

    # Affiche une boîte de dialogue
    messagebox.showerror("Erreur",f"Une erreur est survenue lors de l'importation des librairies. Voir la console pour en savoir +.")

    # Affiche l'erreur dans la console
    print(f"Erreur : {e}\n→ Appuyez sur une touche pour continuer ...")

    # Ecrit l'erreur dans le fichier des logs correspondant
    logs_config.super_logger.error(e)

    # Attend un retour par touche préssée
    m.getch()

try :

    # Lance l'interface depuis le fichier 'new_gui.py'
    gui.ui()

# En cas d'erreur
except Exception as e :

    # Affiche une boîte de dialogue
    messagebox.showerror("Erreur","Une erreur est survenue lors du lancement de l'application. Voir la console pour en savoir +.")

    # Affiche l'erreur dans la console
    print(f"Erreur : {e}\n→ Appuyez sur une touche pour continuer ...")

    # Ecrit l'erreur dans le fichier des logs
    logs_config.super_logger.error(e)

    # Attend un retour par touche préssée
    m.getch()
