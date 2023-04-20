import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

global win_lim
win_lim = 0

def toplevelarecool():
    global win_lim
    top = tk.Toplevel()

    logo = tk.PhotoImage(file="AppImg/win/.png/WinSquared_100x100.png")
    mail = tk.PhotoImage(file="AppImg/Social/gmail-(-65).png")
    snap = tk.PhotoImage(file="AppImg/Social/snapchat-(-65).png")
    inst = tk.PhotoImage(file="AppImg/Social/instagram-(-65).png")
    payp = tk.PhotoImage(file="AppImg/Ext/paypal-(-65).png")

    top.geometry("569x252")
    top.resizable(0,0)
    top.title("À Propos")
    top.configure(background="#d9d9d9", cursor="@AdditionalCursors/default.cur")
    top.iconbitmap("AppImg/win/.ico/AboutLogo.ico")
    
    LogoContainer = tk.Label(top)
    LogoContainer.place(relx=0.035, rely=0.087, height=104, width=104)
    LogoContainer.configure(anchor='w')
    LogoContainer.configure(background="#d9d9d9")
    LogoContainer.configure(compound='left')
    LogoContainer.configure(foreground="#000000")
    LogoContainer.configure(relief="groove")
    LogoContainer.configure(text=None, image=logo)

    AppName = tk.Label(top)
    AppName.place(relx=0.253, rely=0.163, height=21, width=164)
    AppName.configure(anchor='w')
    AppName.configure(background="#d9d9d9")
    AppName.configure(compound='left')
    AppName.configure(font="-family {Yu Gothic UI} -size 11 -weight bold")
    AppName.configure(foreground="#000000")
    AppName.configure(text='''AutoBulletin''')

    AppVersion = tk.Label(top)
    AppVersion.place(relx=0.251, rely=0.238, height=22, width=144)
    AppVersion.configure(anchor='w')
    AppVersion.configure(background="#d9d9d9")
    AppVersion.configure(compound='left')
    AppVersion.configure(foreground="#000000")
    AppVersion.configure(text='''B.0.2''')

    AppCopyright = tk.Label(top)
    AppCopyright.place(relx=0.251, rely=0.333, height=21, width=164)
    AppCopyright.configure(activebackground="#f9f9f9")
    AppCopyright.configure(anchor='w')
    AppCopyright.configure(background="#d9d9d9")
    AppCopyright.configure(compound='left')
    AppCopyright.configure(foreground="#000000")
    AppCopyright.configure(text='''© LABARBE Léo, Mr Imloul''')

    VerticalSep = ttk.Separator(top)
    VerticalSep.place(relx=0.545, rely=0.262,relheight=0.476)
    VerticalSep.configure(orient="vertical")

    DonateButton = tk.Button(top)
    DonateButton.place(relx=0.629, rely=0.742, height=35, width=162)
    DonateButton.configure(activebackground="#d9d9d9")
    DonateButton.configure(activeforeground="black")
    DonateButton.configure(background="#d9d9d9", bd=0, relief='flat', cursor="@AdditionalCursors/pointer.cur")
    DonateButton.configure(compound='left')
    DonateButton.configure(foreground="#000000")
    DonateButton.configure(pady="0")
    DonateButton.configure(text=None, image=payp)

    InstagramButton = tk.Button(top)
    InstagramButton.place(relx=0.629, rely=0.54, height=35, width=162)
    InstagramButton.configure(activebackground="#d9d9d9")
    InstagramButton.configure(activeforeground="black")
    InstagramButton.configure(background="#d9d9d9", bd=0, relief='flat', cursor="@AdditionalCursors/pointer.cur")
    InstagramButton.configure(compound='left')
    InstagramButton.configure(foreground="#000000")
    InstagramButton.configure(pady="0")
    InstagramButton.configure(text=None, image=inst)

    SnapchatButton = tk.Button(top)
    SnapchatButton.place(relx=0.629, rely=0.329, height=35, width=162)
    SnapchatButton.configure(activebackground="#d9d9d9")
    SnapchatButton.configure(activeforeground="black")
    SnapchatButton.configure(background="#d9d9d9", bd=0, relief='flat', cursor="@AdditionalCursors/pointer.cur")
    SnapchatButton.configure(compound='left')
    SnapchatButton.configure(foreground="#000000")
    SnapchatButton.configure(pady="0")
    SnapchatButton.configure(text=None, image=snap)

    GmailButton = tk.Button(top)
    GmailButton.place(relx=0.629, rely=0.127, height=35, width=162)
    GmailButton.configure(activebackground="#d9d9d9")
    GmailButton.configure(activeforeground="black")
    GmailButton.configure(background="#d9d9d9", bd=0, relief='flat', cursor="@AdditionalCursors/pointer.cur")
    GmailButton.configure(compound='left')
    GmailButton.configure(foreground="#000000")
    GmailButton.configure(pady="0")
    GmailButton.configure(text=None, image=mail)

    HorizontalSep = ttk.Separator(top)
    HorizontalSep.place(relx=0.097, rely=0.583,relwidth=0.35)

    Cursors = tk.Label(top)
    Cursors.place(relx=0.035, rely=0.635, height=21, width=104)
    Cursors.configure(activebackground="#f9f9f9")
    Cursors.configure(anchor='w')
    Cursors.configure(background="#d9d9d9")
    Cursors.configure(compound='left')
    Cursors.configure(disabledforeground="#a3a3a3")
    Cursors.configure(font="-family {Yu Gothic UI} -size 9 -weight bold")
    Cursors.configure(foreground="#000000")
    Cursors.configure(highlightbackground="#d9d9d9")
    Cursors.configure(highlightcolor="black")
    Cursors.configure(text='''→ Curseurs :''')

    CursorsUsername = tk.Button(top)
    CursorsUsername.place(relx=0.158, rely=0.635, height=21, width=76)
    CursorsUsername.configure(activebackground="#d9d9d9", activeforeground="#818CFF", bd=0, relief="flat")
    CursorsUsername.configure(anchor='w', cursor="@AdditionalCursors/pointer.cur")
    CursorsUsername.configure(background="#d9d9d9")
    CursorsUsername.configure(compound='left')
    CursorsUsername.configure(font="-family {Segoe UI} -size 9 -underline 1")
    CursorsUsername.configure(foreground="#5662eb")
    CursorsUsername.configure(text='''FlynMaker49''')

    Sounds = tk.Label(top)
    Sounds.place(relx=0.035, rely=0.734, height=21, width=104)
    Sounds.configure(activebackground="#f9f9f9")
    Sounds.configure(anchor='w')
    Sounds.configure(background="#d9d9d9")
    Sounds.configure(compound='left')
    Sounds.configure(disabledforeground="#a3a3a3")
    Sounds.configure(font="-family {Yu Gothic UI} -size 9 -weight bold")
    Sounds.configure(foreground="#000000")
    Sounds.configure(highlightbackground="#d9d9d9")
    Sounds.configure(highlightcolor="black")
    Sounds.configure(text='''→ Sons :''')

    SoundsUsername1 = tk.Button(top)
    SoundsUsername1.place(relx=0.125, rely=0.734, height=21, width=74)
    SoundsUsername1.configure(activebackground="#d9d9d9", activeforeground="#818CFF", bd=0, relief="flat")
    SoundsUsername1.configure(anchor='w', cursor="@AdditionalCursors/pointer.cur")
    SoundsUsername1.configure(background="#d9d9d9")
    SoundsUsername1.configure(compound='left')
    SoundsUsername1.configure(font="-family {Segoe UI} -size 9 -underline 1")
    SoundsUsername1.configure(foreground="#5662eb")
    SoundsUsername1.configure(text='''Leszek Szary''')

    Virgule = tk.Label(top)
    Virgule.place(relx=0.243, rely=0.746, height=21, width=15)
    Virgule.configure(activebackground="#f9f9f9")
    Virgule.configure(anchor='w')
    Virgule.configure(background="#d9d9d9")
    Virgule.configure(compound='left')
    Virgule.configure(disabledforeground="#a3a3a3")
    Virgule.configure(foreground="#000000")
    Virgule.configure(highlightbackground="#d9d9d9")
    Virgule.configure(highlightcolor="black")
    Virgule.configure(text=''',''')

    SoundsUsername2 = tk.Button(top)
    SoundsUsername2.place(relx=0.255, rely=0.734, height=21, width=74)
    SoundsUsername2.configure(activebackground="#d9d9d9", activeforeground="#818CFF", bd=0, relief="flat")
    SoundsUsername2.configure(anchor='w', cursor="@AdditionalCursors/pointer.cur")
    SoundsUsername2.configure(background="#d9d9d9")
    SoundsUsername2.configure(compound='left')
    SoundsUsername2.configure(font="-family {Segoe UI} -size 9 -underline 1")
    SoundsUsername2.configure(foreground="#5662eb")
    SoundsUsername2.configure(text='''Kastenfrosch''')

    Image = tk.Label(top)
    Image.place(relx=0.035, rely=0.833, height=21, width=154)
    Image.configure(activebackground="#f9f9f9")
    Image.configure(anchor='w')
    Image.configure(background="#d9d9d9")
    Image.configure(compound='left')
    Image.configure(disabledforeground="#a3a3a3")
    Image.configure(font="-family {Yu Gothic UI} -size 9 -weight bold")
    Image.configure(foreground="#000000")
    Image.configure(highlightbackground="#d9d9d9")
    Image.configure(highlightcolor="black")
    Image.configure(text='''→ Images Vectorielles :''')

    ImageLink = tk.Button(top)
    ImageLink.place(relx=0.258, rely=0.833, height=21, width=74)
    ImageLink.configure(activebackground="#d9d9d9", activeforeground="#818CFF", bd=0, relief="flat")
    ImageLink.configure(anchor='w', cursor="@AdditionalCursors/pointer.cur")
    ImageLink.configure(background="#d9d9d9")
    ImageLink.configure(compound='left')
    ImageLink.configure(font="-family {Segoe UI} -size 9 -underline 1")
    ImageLink.configure(foreground="#5662eb")
    ImageLink.configure(text='''Flaticon''')

    win_lim = win_lim + 1

    def delete_win_and_add():
        global win_lim
        top.destroy()
        win_lim = win_lim - 1

    top.protocol("WM_DELETE_WINDOW", delete_win_and_add)

    top.mainloop()

def check_availability():
    
    if win_lim == 0 :
        toplevelarecool()
    else :
        print("nope bbc :D")
    

cool_button = tk.Button(root, command=check_availability, text="Check & open :D")
cool_button.pack(pady=20)
root.mainloop()