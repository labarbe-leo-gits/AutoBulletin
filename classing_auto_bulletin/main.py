#######################
# Le programme fourni #               #######################
# ne dispose d'aucune #               # Libre à vous de les #
#       fontion       #               #     implémenter     #
#   d'optimisation    #               #######################
#######################

# Import des librairies
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import pickle
import webbrowser as wb
import logging
import keyboard
import msvcrt as m

# Définition de la clase contenant le setup des logs
class logs_config():

    # Mise en global et définition du formatter pour les logs utilisateur
    global info_formatter
    info_formatter = logging.Formatter('%(levelname)s : %(message)s')

    # Mise en global et définition du formatter pour les logs contenant les erreurs
    global error_formatter
    error_formatter = logging.Formatter('%(levelname)s : %(message)s (file : %(filename)s - line : %(lineno)d)')

    # Définition d'une fonction jouant le rôle de 'logger'
    def info_logger(name, log_file, level=logging.DEBUG):
        """To setup as many loggers as you want"""

        # Définition du fichier d'écriture
        handler = logging.FileHandler(log_file)   

        # Définition du format     
        handler.setFormatter(info_formatter)

        # Configuration du logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        # Retourner le logger
        return logger

    # Définition d'une fonction jouant le rôle de 'logger'
    def error_logger(name, log_file, level=logging.DEBUG):
        """To setup as many loggers as you want"""

        # Définition du fichier d'écriture
        handler_2 = logging.FileHandler(log_file)

        # Définition du format        
        handler_2.setFormatter(error_formatter)

        # Configuration du logger
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler_2)

        # Retourner le logger
        return logger
        
    # Premier 'logger' pour les logs application
    informations = info_logger('first_logger', 'LogsData/app.log')

    # Second 'logger' pour les erreurs de programme
    errors = error_logger('second_logger', 'LogsData/errors.log')

class pickle_data():
    pass

# logs_config.errors.error("hi")

# Définition de la classe pour les raccourcis clavier contenant les fonctions correspondantes
class hotkeys():
    
    # Définition d'une fonction créant des raccourcis clavier avec le module 'keyboard'
    def hotkeys():

        # Définition des raccourcis clavier custom
        keyboard.add_hotkey('ctrl + shift + z', lambda:test())

        # Ouvrir la fenêtre d'informations d'application
        keyboard.add_hotkey('ctrl + i', lambda:print("about app"))

        # Ouvrir la page github
        keyboard.add_hotkey('ctrl + maj + g', lambda:links.GitOpen())

        # Ouvrir la page mediafire
        keyboard.add_hotkey('ctrl + maj + m', lambda:links.MediaOpen())
    
    # Définition d'une fonction pour afficher les raccourcis clavier créer précédement
    def show_hotkeys():

        #lambda:hotkeys().show_hotkeys()

        # Suppression des labels existants
        options_menu.delete("Quitter")
        about.delete("GitHub")
        about.delete("MediaFire")
        hotkeys_menu.delete("Afficher")
        hotkeys_menu.delete("Masquer")

        # Ajout des nouveaux labels avec les raccourcis affichés
        options_menu.add_command(label="Quitter", command=root.quit, accelerator="Alt+F4")
        about.add_command(label="GitHub", command=links.GitOpen, accelerator="Ctrl+Maj+G")
        about.add_command(label="MediaFire", command=links.MediaOpen, accelerator="Ctrl+Maj+M")
        hotkeys_menu.add_command(label="Afficher", command=lambda:ShowHotkeys(), accelerator="Ctrl+Maj+S")
        hotkeys_menu.add_command(label="Masquer", command=lambda:HideHotkeys(), accelerator="Ctrl+Maj+H")
    
    # Définition d'une fonction pour masquer les raccourcis clavier créer précedement
    def HideHotkeys():

        # Suppression des labels existants
        options_menu.delete("Quitter")
        about.delete("GitHub")
        about.delete("MediaFire")
        hotkeys_menu.delete("Afficher")
        hotkeys_menu.delete("Masquer")

        # Ajout des nouveaux labels avec les raccourcis affichés
        options_menu.add_command(label="Quitter", command=root.quit, accelerator=None)
        about.add_command(label="GitHub", command=links.GitOpen, accelerator=None)
        about.add_command(label="MediaFire", command=links.MediaOpen, accelerator=None)
        hotkeys_menu.add_command(label="Afficher", command=lambda:ShowHotkeys(), accelerator=None)
        hotkeys_menu.add_command(label="Masquer", command=lambda:HideHotkeys(), accelerator=None)

# Définition de la classe contenant les liens et les fonctions correspondantes
class links():

    # Définition d'une fonction pour ouvrir la page GitHub du projet
    def GitOpen():
        wb.open("https://github.com/labarbe-leo-gits/AutoBulletin")

    # Définition d'une fonction pour ouvrir la page MediaFire du projet
    def MediaOpen():
        wb.open("https://mediafire.com/folder/8y3wuu514kdyh/Auto_Compl%C3%A9tion_Bulletins")

# Définition de la classe contenant les interfaces utilisateurs dans des fonctions correspondantes
class user_interface():

    # Définition de la fonction pour l'interface principale
    def main_window():

    
        # Définition & propriétés de la fenêtre
        root = tk.Tk()
        root.geometry("452x457")
        root.resizable(0, 0)
        root.title("AutoBulletin - B.0.2")
        root.configure(background="#d9d9d9")

        # Icone de l'interface
        try :
            root.iconbitmap("AppImg/AutoBulletinWinIcon.ico")
        
        # En cas d'erreur
        except Exception as e :
            messagebox.showerror("Erreur","Le chemin d'image spécifié est invalide.\nVoir la console pour en savoir +.")

        # Définition de la barre menu de la fenêtre
        menubar = tk.Menu(root)

        # Création du premier 'sous-menu' de la barre
        options_menu = tk.Menu(menubar, tearoff=0)

        # Ajout de la première commande de la barre pour customiser l'interface
        options_menu.add_command(label="Customiser l'IU")

        # Définition d'une fonction pour afficher les raccourcis dans les menus
        def ShowHotkeys():

            # Suppression des labels existants
            options_menu.delete("Quitter")
            about.delete("GitHub")
            about.delete("MediaFire")
            hotkeys_menu.delete("Afficher")
            hotkeys_menu.delete("Masquer")

            # Ajout des nouveaux labels avec les raccourcis affichés
            options_menu.add_command(label="Quitter", command=root.quit, accelerator="Alt+F4")
            about.add_command(label="GitHub", command=links().GitOpen, accelerator="Ctrl+Maj+G")
            about.add_command(label="MediaFire", command=links().MediaOpen, accelerator="Ctrl+Maj+M")
            hotkeys_menu.add_command(label="Afficher", command=lambda:ShowHotkeys(), accelerator="Ctrl+Maj+S")
            hotkeys_menu.add_command(label="Masquer", command=lambda:HideHotkeys(), accelerator="Ctrl+Maj+H")
        
        def HideHotkeys():

            # Suppression des labels existants
            options_menu.delete("Quitter")
            about.delete("GitHub")
            about.delete("MediaFire")
            hotkeys_menu.delete("Afficher")
            hotkeys_menu.delete("Masquer")

            # Ajout des nouveaux labels avec les raccourcis affichés
            options_menu.add_command(label="Quitter", command=root.quit, accelerator=None)
            about.add_command(label="GitHub", command=links.GitOpen, accelerator=None)
            about.add_command(label="MediaFire", command=links.MediaOpen, accelerator=None)
            hotkeys_menu.add_command(label="Afficher", command=lambda:ShowHotkeys(), accelerator=None)
            hotkeys_menu.add_command(label="Masquer", command=lambda:HideHotkeys(), accelerator=None)

        # Afficher les raccourcis clavier
        keyboard.add_hotkey('ctrl + maj + s', lambda:ShowHotkeys())

        # Cacher les raccourcis clavier
        keyboard.add_hotkey('ctrl + maj + h', lambda:HideHotkeys())

        # Définition d'un menu déroulant dans le menu des Raccourcis Clavier (voir + bas)
        hotkeys_menu = tk.Menu(options_menu, tearoff=0)

        # Ajout de commandes
        hotkeys_menu.add_command(label="Afficher", command=ShowHotkeys)
        hotkeys_menu.add_command(label="Masquer", command=HideHotkeys)
        hotkeys_menu.add_separator()
        hotkeys_menu.add_command(label="Customiser")

        # Définition du menu des Raccourcis Clavier
        options_menu.add_cascade(label="Raccoucis clavier", menu=hotkeys_menu)

        # Ajout de commandes dans le menu des options
        options_menu.add_separator()
        options_menu.add_command(label="Fenêtres au lancement")
        options_menu.add_command(label="MessageBox")

        # Définition d'un menu déroulant dans le menu des Logs (voir + bas)
        logs_menu = tk.Menu(options_menu, tearoff=0)

        # Ajout de commandes
        logs_menu.add_command(label="Config. du format")
        logs_menu.add_command(label="Préférences")

        # Définition du menu des Logs
        options_menu.add_cascade(label="Logs", menu=logs_menu)

        # Ajout de commandes du menu des options
        options_menu.add_separator()
        options_menu.add_command(label="Obtenir de l'aide")
        options_menu.add_separator()
        options_menu.add_command(label="Quitter", command=root.quit, accelerator=None)

        # Création d'un autre 'sous-menu' a la barre principale
        about = tk.Menu(menubar, tearoff=0)

        # Ajout de commandes à ce menu
        about.add_command(label="À propos de l'application")
        about.add_separator()
        about.add_command(label="GitHub", command=links.GitOpen)
        medfire = about.add_command(label="MediaFire", command=links.MediaOpen)

        # Ajout des 'sous-menu' en tant qu'éléments de la barre de menus
        menubar.add_cascade(label="Options", menu=options_menu)  
        menubar.add_cascade(label="Fenêtres")
        menubar.add_cascade(label="À Propos", menu=about)

        # Fixation de la barre de menu à la fenêtre
        root.config(menu=menubar)

        # Définition d'une combobox affichant les classes
        ClassDropDown = ttk.Combobox(root, state="readonly")
        ClassDropDown.place(relx=0.199, rely=0.031, height=20, relwidth=0.584)
        ClassDropDown.config(font="-family {Yu Gothic UI} -size 9")
        ClassDropDown['values']=('Classe','1GT1 - Ledoux', '1GT2 - Ledoux')
        ClassDropDown.current(0)

        # Définition d'une combobox contenant le nom de chaque élève / classe
        StudentDropDown = ttk.Combobox(root, state="readonly") #  values=sorted(liste)
        StudentDropDown.place(relx=0.199, rely=0.092, height=20, relwidth=0.584)
        StudentDropDown.config(font="-family {Yu Gothic UI} -size 9")
        StudentDropDown['values']=('Elèves')
        StudentDropDown.current(0)

        # Définition de l'élément graphique 'séparateur' en haut
        MainSep = ttk.Separator(root)
        MainSep.place(relx=0.268, rely=0.164,  relwidth=0.442)

        # Création d'un bouton de génération
        Gen = tk.Button(root)
        Gen.place(relx=-0.027, rely=0.807, height=34, width=477)
        Gen.configure(background="#d9d9d9")
        Gen.configure(compound='left')
        Gen.configure(font="-family {Yu Gothic UI} -size 10")
        Gen.configure(overrelief='groove')
        Gen.configure(foreground="#000000")
        Gen.configure(text='''Générer l'appréciation''')

        # Création d'un bouton de génération & d'écriture
        GenWrite = tk.Button(root)
        GenWrite.place(relx=-0.027, rely=0.899, height=34, width=477)
        GenWrite.configure(background="#d9d9d9")
        GenWrite.configure(compound='left')
        GenWrite.configure(font="-family {Yu Gothic UI} -size 10")
        GenWrite.configure(overrelief='groove')
        GenWrite.configure(foreground="#000000")
        GenWrite.configure(text='''Générer & écrire l'appréciation''')

        # Définition de l'élément graphique 'séparateur' du bas
        BtnSep = ttk.Separator(root)
        BtnSep.place(relx=0.277, rely=0.777,relwidth=0.442)

        # Définition d'une frame pour le premier classificateur d'appréciation
        TalkativeFrame = tk.Frame(root)
        TalkativeFrame.place(relx=0.022, rely=0.197, relheight=0.339, relwidth=0.299)
        TalkativeFrame.configure(relief='groove')
        TalkativeFrame.configure(borderwidth="2")
        TalkativeFrame.configure(background="#d9d9d9")

        # Texte de la frame définit précedement
        TalkativeText = tk.Label(TalkativeFrame)
        TalkativeText.place(relx=0.111, rely=0.019, height=44, width=104)
        TalkativeText.configure(background="#d9d9d9")
        TalkativeText.configure(compound='left')
        TalkativeText.configure(font="-family {Yu Gothic UI} -size 10")
        TalkativeText.configure(foreground="#000000")
        TalkativeText.configure(text='''Bavardages''')

        # Premier 'radio-button' pour les bavardages modérés
        Moderate = tk.Radiobutton(TalkativeFrame)
        Moderate.place(relx=0.074, rely=0.439, relheight=0.335, relwidth=0.504)
        Moderate.configure(activebackground="#d9d9d9")
        Moderate.configure(anchor='w')
        Moderate.configure(background="#d9d9d9")
        Moderate.configure(compound='left')
        Moderate.configure(font="-family {Segoe UI} -size 8")
        Moderate.configure(foreground="#000000")
        Moderate.configure(justify='left')
        Moderate.configure(text='''Modérés''')

        # Second 'radio-button' pour les bavardages inexistants
        NoTalk = tk.Radiobutton(TalkativeFrame)
        NoTalk.place(relx=0.074, rely=0.639, relheight=0.348, relwidth=0.652)
        NoTalk.configure(activebackground="#d9d9d9")
        NoTalk.configure(anchor='w')
        NoTalk.configure(background="#d9d9d9")
        NoTalk.configure(compound='left')
        NoTalk.configure(foreground="#000000")
        NoTalk.configure(justify='left')
        NoTalk.configure(text='''Inexistants''')

        # Dernier 'radio-button' pour les bavardages très présents
        TalkA_Lot = tk.Radiobutton(TalkativeFrame)
        TalkA_Lot.place(relx=0.074, rely=0.271, relheight=0.271, relwidth=0.726)
        TalkA_Lot.configure(activebackground="#d9d9d9")
        TalkA_Lot.configure(anchor='w')
        TalkA_Lot.configure(background="#d9d9d9")
        TalkA_Lot.configure(compound='left')
        TalkA_Lot.configure(foreground="#000000")
        TalkA_Lot.configure(justify='left')
        TalkA_Lot.configure(text='''Très Présents''')

        # Définition de l'élément graphique 'séparateur' pour la première frame
        FrameSepTalk = ttk.Separator(TalkativeFrame)
        FrameSepTalk.place(relx=0.237, rely=0.271,relwidth=0.519)

        # Deuxième frame pour le sérieux
        SeriousFrame = tk.Frame(root)
        SeriousFrame.place(relx=0.679, rely=0.197, relheight=0.339, relwidth=0.299)
        SeriousFrame.configure(borderwidth="2")
        SeriousFrame.configure(relief="groove")
        SeriousFrame.configure(background="#d9d9d9")

        Label3_1 = tk.Label(SeriousFrame)
        Label3_1.place(relx=0.111, rely=0.019, height=44, width=104)
        Label3_1.configure(activebackground="#f9f9f9")
        Label3_1.configure(background="#d9d9d9")
        Label3_1.configure(compound='left')
        Label3_1.configure(disabledforeground="#a3a3a3")
        Label3_1.configure(font="-family {Yu Gothic UI} -size 10")
        Label3_1.configure(foreground="#000000")
        Label3_1.configure(highlightbackground="#d9d9d9")
        Label3_1.configure(highlightcolor="black")
        Label3_1.configure(text='''Sérieux''')

        Radiobutton1_3 = tk.Radiobutton(SeriousFrame)
        Radiobutton1_3.place(relx=0.074, rely=0.335, relheight=0.529, relwidth=0.874)
        Radiobutton1_3.configure(activebackground="beige")
        Radiobutton1_3.configure(activeforeground="black")
        Radiobutton1_3.configure(anchor='w')
        Radiobutton1_3.configure(background="#d9d9d9")
        Radiobutton1_3.configure(compound='left')
        Radiobutton1_3.configure(disabledforeground="#a3a3a3")
        Radiobutton1_3.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_3.configure(foreground="#000000")
        Radiobutton1_3.configure(highlightbackground="#d9d9d9")
        Radiobutton1_3.configure(highlightcolor="black")
        Radiobutton1_3.configure(justify='left')
        Radiobutton1_3.configure(selectcolor="#d9d9d9")
        Radiobutton1_3.configure(text='''Dissipé (Rarement)''')

        Radiobutton1_1_1 = tk.Radiobutton(SeriousFrame)
        Radiobutton1_1_1.place(relx=0.074, rely=0.639, relheight=0.348, relwidth=0.874)
        Radiobutton1_1_1.configure(activebackground="beige")
        Radiobutton1_1_1.configure(activeforeground="black")
        Radiobutton1_1_1.configure(anchor='w')
        Radiobutton1_1_1.configure(background="#d9d9d9")
        Radiobutton1_1_1.configure(compound='left')
        Radiobutton1_1_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_1_1.configure(foreground="#000000")
        Radiobutton1_1_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_1_1.configure(highlightcolor="black")
        Radiobutton1_1_1.configure(justify='left')
        Radiobutton1_1_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_1_1.configure(text='''Souvent Ailleurs''')

        Radiobutton1_2_1 = tk.Radiobutton(SeriousFrame)
        Radiobutton1_2_1.place(relx=0.074, rely=0.271, relheight=0.271, relwidth=0.726)
        Radiobutton1_2_1.configure(activebackground="beige")
        Radiobutton1_2_1.configure(activeforeground="black")
        Radiobutton1_2_1.configure(anchor='w')
        Radiobutton1_2_1.configure(background="#d9d9d9")
        Radiobutton1_2_1.configure(compound='left')
        Radiobutton1_2_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_1.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_1.configure(foreground="#000000")
        Radiobutton1_2_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_1.configure(highlightcolor="black")
        Radiobutton1_2_1.configure(justify='left')
        Radiobutton1_2_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_1.configure(text='''Sérieux''')

        TSeparator3_1 = ttk.Separator(SeriousFrame)
        TSeparator3_1.place(relx=0.215, rely=0.271,relwidth=0.519)

        Frame1_2 = tk.Frame(root)
        Frame1_2.place(relx=0.352, rely=0.197, relheight=0.339, relwidth=0.299)
        Frame1_2.configure(relief='groove')
        Frame1_2.configure(borderwidth="2")
        Frame1_2.configure(relief="groove")
        Frame1_2.configure(background="#d9d9d9")
        Frame1_2.configure(highlightbackground="#d9d9d9")
        Frame1_2.configure(highlightcolor="black")

        Label3_2 = tk.Label(Frame1_2)
        Label3_2.place(relx=0.111, rely=0.019, height=44, width=104)
        Label3_2.configure(activebackground="#f9f9f9")
        Label3_2.configure(background="#d9d9d9")
        Label3_2.configure(compound='left')
        Label3_2.configure(disabledforeground="#a3a3a3")
        Label3_2.configure(font="-family {Yu Gothic UI} -size 10")
        Label3_2.configure(foreground="#000000")
        Label3_2.configure(highlightbackground="#d9d9d9")
        Label3_2.configure(highlightcolor="black")
        Label3_2.configure(text='''Assiduitée''')
        
        Radiobutton1_4 = tk.Radiobutton(Frame1_2)
        Radiobutton1_4.place(relx=0.074, rely=0.439, relheight=0.335, relwidth=0.874)
        Radiobutton1_4.configure(activebackground="beige")
        Radiobutton1_4.configure(activeforeground="black")
        Radiobutton1_4.configure(anchor='w')
        Radiobutton1_4.configure(background="#d9d9d9")
        Radiobutton1_4.configure(compound='left')
        Radiobutton1_4.configure(disabledforeground="#a3a3a3")
        Radiobutton1_4.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_4.configure(foreground="#000000")
        Radiobutton1_4.configure(highlightbackground="#d9d9d9")
        Radiobutton1_4.configure(highlightcolor="black")
        Radiobutton1_4.configure(justify='left')
        Radiobutton1_4.configure(selectcolor="#d9d9d9")
        Radiobutton1_4.configure(text='''Quelques Oublis''')
        Radiobutton1_4.configure()

        Radiobutton1_1_2 = tk.Radiobutton(Frame1_2)
        Radiobutton1_1_2.place(relx=0.074, rely=0.639, relheight=0.348, relwidth=0.874)
        Radiobutton1_1_2.configure(activebackground="beige")
        Radiobutton1_1_2.configure(activeforeground="black")
        Radiobutton1_1_2.configure(anchor='w')
        Radiobutton1_1_2.configure(background="#d9d9d9")
        Radiobutton1_1_2.configure(compound='left')
        Radiobutton1_1_2.configure(disabledforeground="#a3a3a3")
        Radiobutton1_1_2.configure(foreground="#000000")
        Radiobutton1_1_2.configure(highlightbackground="#d9d9d9")
        Radiobutton1_1_2.configure(highlightcolor="black")
        Radiobutton1_1_2.configure(justify='left')
        Radiobutton1_1_2.configure(selectcolor="#d9d9d9")
        Radiobutton1_1_2.configure(text='''Non-Assidu''')
        Radiobutton1_1_2.configure()

        Radiobutton1_2_2 = tk.Radiobutton(Frame1_2)
        Radiobutton1_2_2.place(relx=0.074, rely=0.271, relheight=0.271, relwidth=0.726)
        Radiobutton1_2_2.configure(activebackground="beige")
        Radiobutton1_2_2.configure(activeforeground="black")
        Radiobutton1_2_2.configure(anchor='w')
        Radiobutton1_2_2.configure(background="#d9d9d9")
        Radiobutton1_2_2.configure(compound='left')
        Radiobutton1_2_2.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_2.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_2.configure(foreground="#000000")
        Radiobutton1_2_2.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_2.configure(highlightcolor="black")
        Radiobutton1_2_2.configure(justify='left')
        Radiobutton1_2_2.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_2.configure(text='''Assidu''')
        Radiobutton1_2_2.configure()

        TSeparator3_2 = ttk.Separator(Frame1_2)
        TSeparator3_2.place(relx=0.237, rely=0.271,relwidth=0.519)

        Frame2 = tk.Frame(root)
        Frame2.place(relx=0.022, rely=0.547, relheight=0.204, relwidth=0.467)
        Frame2.configure(relief='groove')
        Frame2.configure(borderwidth="2")
        Frame2.configure(relief="groove")
        Frame2.configure(background="#d9d9d9")
        Frame2.configure(highlightbackground="#d9d9d9")
        Frame2.configure(highlightcolor="black")

        Label1 = tk.Label(Frame2)
        Label1.place(relx=0.19, rely=0.108, height=21, width=124)
        Label1.configure(activebackground="#f9f9f9")
        Label1.configure(background="#d9d9d9")
        Label1.configure(compound='left')
        Label1.configure(disabledforeground="#a3a3a3")
        Label1.configure(font="-family {Yu Gothic UI} -size 10")
        Label1.configure(foreground="#000000")
        Label1.configure(highlightbackground="#d9d9d9")
        Label1.configure(highlightcolor="black")
        Label1.configure(text='''Participation''')

        TSeparator3_2_1 = ttk.Separator(Frame2)
        TSeparator3_2_1.place(relx=0.318, rely=0.387,relwidth=0.332)

        Radiobutton1_2_3 = tk.Radiobutton(Frame2)
        Radiobutton1_2_3.place(relx=0.081, rely=0.409, relheight=0.344, relwidth=0.37)
        Radiobutton1_2_3.configure(activebackground="beige")
        Radiobutton1_2_3.configure(activeforeground="black")
        Radiobutton1_2_3.configure(anchor='w')
        Radiobutton1_2_3.configure(background="#d9d9d9")
        Radiobutton1_2_3.configure(compound='left')
        Radiobutton1_2_3.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3.configure(foreground="#000000")
        Radiobutton1_2_3.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3.configure(highlightcolor="black")
        Radiobutton1_2_3.configure(justify='left')
        Radiobutton1_2_3.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3.configure(text='''Régulière''')
        Radiobutton1_2_3.configure()

        Radiobutton1_2_3_1 = tk.Radiobutton(Frame2)
        Radiobutton1_2_3_1.place(relx=0.081, rely=0.688, relheight=0.237, relwidth=0.37)
        Radiobutton1_2_3_1.configure(activebackground="beige")
        Radiobutton1_2_3_1.configure(activeforeground="black")
        Radiobutton1_2_3_1.configure(anchor='w')
        Radiobutton1_2_3_1.configure(background="#d9d9d9")
        Radiobutton1_2_3_1.configure(compound='left')
        Radiobutton1_2_3_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_1.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_1.configure(foreground="#000000")
        Radiobutton1_2_3_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_1.configure(highlightcolor="black")
        Radiobutton1_2_3_1.configure(justify='left')
        Radiobutton1_2_3_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_1.configure(text='''Hésitante''')
        Radiobutton1_2_3_1.configure()

        Radiobutton1_2_3_2 = tk.Radiobutton(Frame2)
        Radiobutton1_2_3_2.place(relx=0.521, rely=0.57, relheight=0.237, relwidth=0.417)
        Radiobutton1_2_3_2.configure(activebackground="beige")
        Radiobutton1_2_3_2.configure(activeforeground="black")
        Radiobutton1_2_3_2.configure(anchor='w')
        Radiobutton1_2_3_2.configure(background="#d9d9d9")
        Radiobutton1_2_3_2.configure(compound='left')
        Radiobutton1_2_3_2.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_2.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_2.configure(foreground="#000000")
        Radiobutton1_2_3_2.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_2.configure(highlightcolor="black")
        Radiobutton1_2_3_2.configure(justify='left')
        Radiobutton1_2_3_2.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_2.configure(text='''Inexistante''')
        Radiobutton1_2_3_2.configure()

        TSeparator2 = ttk.Separator(Frame2)
        TSeparator2.place(relx=0.474, rely=0.516,relheight=0.323)
        TSeparator2.configure(orient="vertical")

        Frame2_2 = tk.Frame(root)
        Frame2_2.place(relx=0.511, rely=0.547, relheight=0.204, relwidth=0.467)
        Frame2_2.configure(relief='groove')
        Frame2_2.configure(borderwidth="2")
        Frame2_2.configure(relief="groove")
        Frame2_2.configure(background="#d9d9d9")
        Frame2_2.configure(highlightbackground="#d9d9d9")
        Frame2_2.configure(highlightcolor="black")

        Label1_1 = tk.Label(Frame2_2)
        Label1_1.place(relx=0.19, rely=0.108, height=21, width=124)
        Label1_1.configure(activebackground="#f9f9f9")
        Label1_1.configure(background="#d9d9d9")
        Label1_1.configure(compound='left')
        Label1_1.configure(disabledforeground="#a3a3a3")
        Label1_1.configure(font="-family {Yu Gothic UI} -size 10")
        Label1_1.configure(foreground="#000000")
        Label1_1.configure(highlightbackground="#d9d9d9")
        Label1_1.configure(highlightcolor="black")
        Label1_1.configure(text='''Résultats''')

        TSeparator3_2_1_1 = ttk.Separator(Frame2_2)
        TSeparator3_2_1_1.place(relx=0.318, rely=0.387,relwidth=0.332)

        Radiobutton1_2_3_3 = tk.Radiobutton(Frame2_2)
        Radiobutton1_2_3_3.place(relx=0.081, rely=0.409, relheight=0.344, relwidth=0.37)
        Radiobutton1_2_3_3.configure(activebackground="beige")
        Radiobutton1_2_3_3.configure(activeforeground="black")
        Radiobutton1_2_3_3.configure(anchor='w')
        Radiobutton1_2_3_3.configure(background="#d9d9d9")
        Radiobutton1_2_3_3.configure(compound='left')
        Radiobutton1_2_3_3.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_3.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_3.configure(foreground="#000000")
        Radiobutton1_2_3_3.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_3.configure(highlightcolor="black")
        Radiobutton1_2_3_3.configure(justify='left')
        Radiobutton1_2_3_3.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_3.configure(text='''Excellents''')
        Radiobutton1_2_3_3.configure()

        Radiobutton1_2_3_1_1 = tk.Radiobutton(Frame2_2)
        Radiobutton1_2_3_1_1.place(relx=0.081, rely=0.688, relheight=0.237, relwidth=0.37)
        Radiobutton1_2_3_1_1.configure(activebackground="beige")
        Radiobutton1_2_3_1_1.configure(activeforeground="black")
        Radiobutton1_2_3_1_1.configure(anchor='w')
        Radiobutton1_2_3_1_1.configure(background="#d9d9d9")
        Radiobutton1_2_3_1_1.configure(compound='left')
        Radiobutton1_2_3_1_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_1_1.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_1_1.configure(foreground="#000000")
        Radiobutton1_2_3_1_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_1_1.configure(highlightcolor="black")
        Radiobutton1_2_3_1_1.configure(justify='left')
        Radiobutton1_2_3_1_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_1_1.configure(text='''Bon''')
        Radiobutton1_2_3_1_1.configure()

        Radiobutton1_2_3_2_1 = tk.Radiobutton(Frame2_2)
        Radiobutton1_2_3_2_1.place(relx=0.521, rely=0.473, relheight=0.237, relwidth=0.417)
        Radiobutton1_2_3_2_1.configure(activebackground="beige")
        Radiobutton1_2_3_2_1.configure(activeforeground="black")
        Radiobutton1_2_3_2_1.configure(anchor='w')
        Radiobutton1_2_3_2_1.configure(background="#d9d9d9")
        Radiobutton1_2_3_2_1.configure(compound='left')
        Radiobutton1_2_3_2_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_2_1.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_2_1.configure(foreground="#000000")
        Radiobutton1_2_3_2_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_2_1.configure(highlightcolor="black")
        Radiobutton1_2_3_2_1.configure(justify='left')
        Radiobutton1_2_3_2_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_2_1.configure(text='''Efforts''')
        Radiobutton1_2_3_2_1.configure()

        TSeparator2_1 = ttk.Separator(Frame2_2)
        TSeparator2_1.place(relx=0.474, rely=0.516,relheight=0.323)
        TSeparator2_1.configure(orient="vertical")
        
        Radiobutton1_2_3_2_1_1 = tk.Radiobutton(Frame2_2)
        Radiobutton1_2_3_2_1_1.place(relx=0.521, rely=0.699, relheight=0.237, relwidth=0.417)
        Radiobutton1_2_3_2_1_1.configure(activebackground="beige")
        Radiobutton1_2_3_2_1_1.configure(activeforeground="black")
        Radiobutton1_2_3_2_1_1.configure(anchor='w')
        Radiobutton1_2_3_2_1_1.configure(background="#d9d9d9")
        Radiobutton1_2_3_2_1_1.configure(compound='left')
        Radiobutton1_2_3_2_1_1.configure(disabledforeground="#a3a3a3")
        Radiobutton1_2_3_2_1_1.configure(font="-family {Segoe UI} -size 8")
        Radiobutton1_2_3_2_1_1.configure(foreground="#000000")
        Radiobutton1_2_3_2_1_1.configure(highlightbackground="#d9d9d9")
        Radiobutton1_2_3_2_1_1.configure(highlightcolor="black")
        Radiobutton1_2_3_2_1_1.configure(justify='left')
        Radiobutton1_2_3_2_1_1.configure(selectcolor="#d9d9d9")
        Radiobutton1_2_3_2_1_1.configure(text='''Insuffisants''')
        Radiobutton1_2_3_2_1_1.configure()

        root.mainloop()

# Appel de l'interface
user_interface.main_window()
