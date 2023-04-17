import tkinter as tk

def win(title, content):
    top = tk.Toplevel()
    top.geometry("410x225")
    top.resizable(1,  1)
    top.title(title)
    top.configure(background="#d9d9d9")

    Text1 = tk.Text(top)
    Text1.place(relx=0.017, rely=0.044, relheight=0.907, relwidth=0.961)
    Text1.configure(background="#fafafa")
    Text1.configure(font="TkTextFont")
    Text1.configure(foreground="black")
    Text1.configure(insertbackground="black")
    Text1.configure(selectbackground="#505050")
    Text1.configure(selectforeground="white")
    Text1.configure(wrap="word")

    if content == 'Licence':
        Text1.insert("1.0", "Licence logicielle")
    elif content == 'History':
        Text1.insert("1.0", "Historique des actions")

    top.mainloop()

#win("Licence", "Licence")