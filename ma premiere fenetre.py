from tkinter import *

# ma fenetre
window = Tk()

# caractéristique de la fenetre
window.title("Pierre, Papier, Ciseaux !!!")
window.geometry("600x600")
window.maxsize()
window.iconbitmap("51V-YSNt-iL.ico")
window.config(background = '#258521')

# texte
label_title = Label(window, text = "Bonjour Christophe !!!", font = ("courrier", 40), bg = 'red', fg = 'black')
label_title.pack(expand = YES)

# afficher
window.mainloop()
