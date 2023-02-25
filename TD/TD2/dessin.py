import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")

def carre():
    pass
def cercle():
    pass
def couleur():
    pass
def croix():
    pass

canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1,rowspan=3, column=1)
bouton_couleur = tk.Button(text='choisir une couleur', command=couleur)
bouton_cercle = tk.Button(text='Cercle',command=cercle)
bouton_carre=tk.Button( text='carre', command=carre)
button_croix=tk.Button( text='croix', command= croix)

bouton_couleur.grid(row=0, column=1)
bouton_carre.grid(row=1,column=0)
bouton_cercle.grid(row=2, column=0)
button_croix.grid(row=3, column=0)

root.mainloop()