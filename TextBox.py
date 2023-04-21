import tkinter as tk
import tkinter.scrolledtext as scrolledtext

def win(title, content):
    top = tk.Toplevel()
    top.geometry("410x225")
    top.resizable(0,0)
    top.iconbitmap("AppImg/win/.ico/Licence.ico")
    top.title(title)
    top.configure(background="#d9d9d9")

    Text1 = scrolledtext.ScrolledText(top)
    Text1.place(relx=0.017, rely=0.044, relheight=0.907, relwidth=0.961)
    Text1.configure(background="#fafafa")
    Text1.configure(font="TkTextFont")
    Text1.configure(foreground="black")
    Text1.configure(insertbackground="black")
    Text1.configure(selectbackground="#505050")
    Text1.configure(selectforeground="white")
    Text1.configure(wrap="word")

    try:
  
        # open the file in 'read mode' so we can read the file contents, the open 
        # function will return a file object
        file = open("Data/Licence.txt", "r")

        # the file object has a read() method that will return all the file contents
        # as a string when we call it like we do below 
        contents = file.read()

        # print out the contents of the string
        print(contents)

        # close the file
        file.close()

        # if an exception is raised in the try block we can handle the exception 
        # with this except block
    except:

        # output an error message for the user
        print("Error reading file.")

    if content == 'Licence':
        Text1.insert("1.0", contents)
    elif content == 'History':
        Text1.insert("1.0", "Historique des actions")

    top.mainloop()

win("Licence", "Licence")