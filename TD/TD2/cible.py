import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1, column=1)
rayon = int(input('chiffre'))

for i in rayon:
    cercle = canvas.create_oval((0, 0), (500, 500), fill="blue") 
    cercle = canvas.create_oval((20, 20), (480, 480), fill="green") 
    cercle = canvas.create_oval((40, 40), (460, 460), fill="black" ) 
    cercle = canvas.create_oval((60, 60), (440, 440), fill="yellow") 
    cercle = canvas.create_oval((80, 80), (420, 420), fill="magenta") 
    cercle = canvas.create_oval((100, 100), (400, 400), fill="red" ) 


root.mainloop()