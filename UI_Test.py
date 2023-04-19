import tkinter as tk
import tkinter.ttk as ttk

top = tk.Toplevel()

top.geometry("569x252+324+205")
top.minsize(120, 1)
top.maxsize(1284, 701)
top.resizable(1,1)
top.title("Toplevel 0")
top.configure(background="#d9d9d9")
top.configure(highlightbackground="#d9d9d9")
top.configure(highlightcolor="black")
 
LogoContainer = tk.Label(top)
LogoContainer.place(relx=0.035, rely=0.087, height=104, width=104)
LogoContainer.configure(activebackground="#f9f9f9")
LogoContainer.configure(anchor='w')
LogoContainer.configure(background="#d9d9d9")
LogoContainer.configure(compound='left')
LogoContainer.configure(disabledforeground="#a3a3a3")
LogoContainer.configure(foreground="#000000")
LogoContainer.configure(highlightbackground="#d9d9d9")
LogoContainer.configure(highlightcolor="black")
LogoContainer.configure(relief="groove")
LogoContainer.configure(text='''Label''')
AppName = tk.Label(top)
AppName.place(relx=0.253, rely=0.163, height=21, width=164)
AppName.configure(activebackground="#f9f9f9")
AppName.configure(anchor='w')
AppName.configure(background="#d9d9d9")
AppName.configure(compound='left')
AppName.configure(disabledforeground="#a3a3a3")
AppName.configure(font="-family {Yu Gothic UI} -size 11 -weight bold")
AppName.configure(foreground="#000000")
AppName.configure(highlightbackground="#d9d9d9")
AppName.configure(highlightcolor="black")
AppName.configure(text='''AutoBulletin''')
AppVersion = tk.Label(top)
AppVersion.place(relx=0.251, rely=0.238, height=22, width=144)
AppVersion.configure(activebackground="#f9f9f9")
AppVersion.configure(anchor='w')
AppVersion.configure(background="#d9d9d9")
AppVersion.configure(compound='left')
AppVersion.configure(disabledforeground="#a3a3a3")
AppVersion.configure(foreground="#000000")
AppVersion.configure(highlightbackground="#d9d9d9")
AppVersion.configure(highlightcolor="black")
AppVersion.configure(text='''B.0.2''')
AppCopyright = tk.Label(top)
AppCopyright.place(relx=0.251, rely=0.333, height=21, width=164)
AppCopyright.configure(activebackground="#f9f9f9")
AppCopyright.configure(anchor='w')
AppCopyright.configure(background="#d9d9d9")
AppCopyright.configure(compound='left')
AppCopyright.configure(disabledforeground="#a3a3a3")
AppCopyright.configure(foreground="#000000")
AppCopyright.configure(highlightbackground="#d9d9d9")
AppCopyright.configure(highlightcolor="black")
AppCopyright.configure(text='''© LABARBE Léo, Mr Imloul''')
VerticalSep = ttk.Separator(top)
VerticalSep.place(relx=0.545, rely=0.262,relheight=0.476)
VerticalSep.configure(orient="vertical")
DonateButton = tk.Button(top)
DonateButton.place(relx=0.629, rely=0.742, height=35, width=162)
DonateButton.configure(activebackground="beige")
DonateButton.configure(activeforeground="black")
DonateButton.configure(background="#d9d9d9")
DonateButton.configure(compound='left')
DonateButton.configure(disabledforeground="#a3a3a3")
DonateButton.configure(foreground="#000000")
DonateButton.configure(highlightbackground="#d9d9d9")
DonateButton.configure(highlightcolor="black")
DonateButton.configure(pady="0")
DonateButton.configure(text='''Button''')
InstagramButton = tk.Button(top)
InstagramButton.place(relx=0.629, rely=0.532, height=35, width=162)
InstagramButton.configure(activebackground="beige")
InstagramButton.configure(activeforeground="black")
InstagramButton.configure(background="#d9d9d9")
InstagramButton.configure(compound='left')
InstagramButton.configure(disabledforeground="#a3a3a3")
InstagramButton.configure(foreground="#000000")
InstagramButton.configure(highlightbackground="#d9d9d9")
InstagramButton.configure(highlightcolor="black")
InstagramButton.configure(pady="0")
InstagramButton.configure(text='''Button''')
SnapchatButton = tk.Button(top)
SnapchatButton.place(relx=0.629, rely=0.333, height=35, width=162)
SnapchatButton.configure(activebackground="beige")
SnapchatButton.configure(activeforeground="black")
SnapchatButton.configure(background="#d9d9d9")
SnapchatButton.configure(compound='left')
SnapchatButton.configure(disabledforeground="#a3a3a3")
SnapchatButton.configure(foreground="#000000")
SnapchatButton.configure(highlightbackground="#d9d9d9")
SnapchatButton.configure(highlightcolor="black")
SnapchatButton.configure(pady="0")
SnapchatButton.configure(text='''Button''')
GmailButton = tk.Button(top)
GmailButton.place(relx=0.629, rely=0.127, height=35, width=162)
GmailButton.configure(activebackground="beige")
GmailButton.configure(activeforeground="black")
GmailButton.configure(background="#d9d9d9")
GmailButton.configure(compound='left')
GmailButton.configure(disabledforeground="#a3a3a3")
GmailButton.configure(foreground="#000000")
GmailButton.configure(highlightbackground="#d9d9d9")
GmailButton.configure(highlightcolor="black")
GmailButton.configure(pady="0")
GmailButton.configure(text='''Button''')
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
CursorsUsername = tk.Label(top)
CursorsUsername.place(relx=0.158, rely=0.635, height=21, width=74)
CursorsUsername.configure(activebackground="#f9f9f9")
CursorsUsername.configure(anchor='w')
CursorsUsername.configure(background="#d9d9d9")
CursorsUsername.configure(compound='left')
CursorsUsername.configure(disabledforeground="#a3a3a3")
CursorsUsername.configure(font="-family {Segoe UI} -size 9 -underline 1")
CursorsUsername.configure(foreground="#5662eb")
CursorsUsername.configure(highlightbackground="#d9d9d9")
CursorsUsername.configure(highlightcolor="black")
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
SoundsUsername1 = tk.Label(top)
SoundsUsername1.place(relx=0.125, rely=0.734, height=21, width=74)
SoundsUsername1.configure(activebackground="#f9f9f9")
SoundsUsername1.configure(anchor='w')
SoundsUsername1.configure(background="#d9d9d9")
SoundsUsername1.configure(compound='left')
SoundsUsername1.configure(disabledforeground="#a3a3a3")
SoundsUsername1.configure(font="-family {Segoe UI} -size 9 -underline 1")
SoundsUsername1.configure(foreground="#5662eb")
SoundsUsername1.configure(highlightbackground="#d9d9d9")
SoundsUsername1.configure(highlightcolor="black")
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
SoundsUsername2 = tk.Label(top)
SoundsUsername2.place(relx=0.255, rely=0.734, height=21, width=74)
SoundsUsername2.configure(activebackground="#f9f9f9")
SoundsUsername2.configure(anchor='w')
SoundsUsername2.configure(background="#d9d9d9")
SoundsUsername2.configure(compound='left')
SoundsUsername2.configure(disabledforeground="#a3a3a3")
SoundsUsername2.configure(font="-family {Segoe UI} -size 9 -underline 1")
SoundsUsername2.configure(foreground="#5662eb")
SoundsUsername2.configure(highlightbackground="#d9d9d9")
SoundsUsername2.configure(highlightcolor="black")
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
ImageLink = tk.Label(top)
ImageLink.place(relx=0.258, rely=0.833, height=21, width=74)
ImageLink.configure(activebackground="#f9f9f9")
ImageLink.configure(anchor='w')
ImageLink.configure(background="#d9d9d9")
ImageLink.configure(compound='left')
ImageLink.configure(disabledforeground="#a3a3a3")
ImageLink.configure(font="-family {Segoe UI} -size 9 -underline 1")
ImageLink.configure(foreground="#5662eb")
ImageLink.configure(highlightbackground="#d9d9d9")
ImageLink.configure(highlightcolor="black")
ImageLink.configure(text='''Flaticon''')

top.mainloop()