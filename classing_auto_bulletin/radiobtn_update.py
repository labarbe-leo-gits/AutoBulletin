# Script non optimisé

import tkinter as tk
 
class Window:
    def __init__(self, master):
        self.master = master
 
        # Frame
        self.frame = tk.Frame(self.master, width = 200, height = 200)
        self.frame.pack()
    
        # Bavardages
        self.label = tk.Label(self.frame, text="Bavardages")
        self.label.pack()

        self.var1 = tk.IntVar()

        self.radio = tk.Radiobutton(self.frame, variable = self.var1, value = 1, text = "Oui", command = self.bavardages)
        self.radio.pack()

        self.radio2 = tk.Radiobutton(self.frame, variable = self.var1, value = 2, text = "Non", command = self.bavardages)
        self.radio2.pack()

        # Sérieux
        self.label2 = tk.Label(self.frame, text="Sérieux")
        self.label2.pack()

        self.var2 = tk.IntVar()

        self.radio3 = tk.Radiobutton(self.frame, variable = self.var2, value = 1, text="Oui", command=self.serious)
        self.radio3.pack()

        self.radio4 = tk.Radiobutton(self.frame, variable = self.var2, value = 2, text="Non", command=self.serious)
        self.radio4.pack()

        # Participe
        self.label3 = tk.Label(self.frame, text="L'élève participe")
        self.label3.pack()

        self.var3 = tk.IntVar()

        self.radio5 = tk.Radiobutton(self.frame, variable = self.var3, value = 1, text="Oui", command=self.participation)
        self.radio5.pack()

        self.radio6 = tk.Radiobutton(self.frame, variable = self.var3, value = 2, text="Non", command=self.participation)
        self.radio6.pack()

        # Résultats
        self.label4 = tk.Label(self.frame, text="L'élève participe")
        self.label4.pack()

        self.var4 = tk.IntVar()

        self.radio6 = tk.Radiobutton(self.frame, variable = self.var3, value = 1, text="Oui", command=self.participation)
        self.radio6.pack()

        self.radio7 = tk.Radiobutton(self.frame, variable = self.var3, value = 2, text="Non", command=self.participation)
        self.radio7.pack()


 
 
    def bavardages(self):
        if self.var1.get() == 1:
            print("'Bavardages' set to True")
        elif self.var1.get() == 2:
            print("'Bavardages' set to False")
    
    def serious(self):
        if self.var2.get() == 1:
            print("'Sérieux' set to True")
        elif self.var2.get() == 2:
            print("'Sérieux' set to False")
    
    def participation(self):
        if self.var3.get() == 1:
            print("'Participe' set to True")
        elif self.var3.get() == 2:
            print("'Participe' set to False")
 
 
root = tk.Tk()
root.title("Auto-Bulletin - UI.B.0.1")
root.resizable(0, 0)
root.geometry('300x500')
 
window = Window(root)
root.mainloop()