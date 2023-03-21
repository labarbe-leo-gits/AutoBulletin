# Import
import keyboard
import os

# Changement de répertoire
os.path.join("../..")

# Import d'un script local
import AdditionalScripts.HiddenData.links_opening as links
from AdditionalScripts.GUI.new_gui import *

def test():
    print("hey ~")

# Pour les raccourcis "Afficher les raccourcis" & "Cacher les raccourcis", voir le fichier 'new_gui.py'
# Ces derniers on été déplacés là-bas en raison de problèmes d'import

# Définition des raccourcis clavier custom
keyboard.add_hotkey('ctrl + shift + z', lambda:test())

# Ouvrir la fenêtre d'informations d'application
keyboard.add_hotkey('ctrl + i', lambda:print("about app"))

# Ouvrir la page github
keyboard.add_hotkey('ctrl + maj + g', lambda:links.GitOpen())

# Ouvrir la page mediafire
keyboard.add_hotkey('ctrl + maj + m', lambda:links.MediaOpen())
