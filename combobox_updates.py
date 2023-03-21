import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a class:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
selected_student = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)
student_cb = ttk.Combobox(root, textvariable=selected_student)

# get first 3 letters of every month name
month_cb['values'] = ["1GT1", "1GT2"]

default_val = ["Choisissez une classe"]

student_cb['values'] = default_val

# prevent typing a value
month_cb['state'] = 'readonly'
student_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)
month_cb.set('Classe')

student_cb.pack(fill = tk.X, padx=5, pady=10)
student_cb.set('Elèves')

Complete1GT1List = ["ABBASSI-BRIOZZO Noham", "AININE Laetitia", "BADACHE Mohamed", "BELHADJ Imene", "BELHANAFI Nihad", "BEN ATMANE Kenza", "BENYAHIA Mouna", "BOUHANIA Mohamed", "DEGUI Soraya Milane", "DIALLO Medina", "DINLER Okan", "HADDAD Hamza", "HAMZA Evane", "HUGUENIN NEEKHUNTOD Kim", "KORCHID Rami", "KOUNAIDIL Chaima", "LABARBE Léo", "LIS Xavier", "MARTINS CASEIRO Nourhane", "MENANA Imane Teriza", "NGONO Seraphine", "RODRIGUES FARIA ALVES Laura", "TACHI Wacil", "TALBI Sihame"]

names_1GT1 = ["Kenza", "Léo", "Mouna"]
names_1GT2 = ["Jacques"]


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    print(selected_month.get())

    if selected_month.get() == '1GT1':
        student_cb.set('')
        student_cb['values'] = names_1GT1

    elif selected_month.get() == '1GT2':
        student_cb.set('')
        student_cb['values'] = names_1GT2

    else :
        student_cb['values'] = default_val

def student_changed(event):
    print(selected_student.get())

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()