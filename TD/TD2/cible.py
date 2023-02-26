import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1, column=1)

x0=0
y0=0
x1= 500
y1 = 500

cercle = canvas.create_oval((x0, y0), (x1, x1), fill="blue") 
cercle = canvas.create_oval((x0+20, y0+20), (x1-20, y1-20), fill="green") 
cercle = canvas.create_oval((x0+40, y0+40), (x1-40, y1-40), fill="black" ) 



root.mainloop()



i = 0
while i < 2:
    canvas.create_oval((x0+20, y0+20), (x1-20, y1 -20), fill= coul[i])
    i = i + 1


import tkinter as tk

root = tk.Tk()



canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1, column=1)
coul = ["red", "green", "blue", "cyan", "yellow"]

x0= 0
y0=0
x1= 500
y1 = 500

n = 5


c = canvas.create_oval((x0, y0), (x1, x1), fill= coul[0]) 
for el in range(1, n):
    for i in coul:
        canvas.create_oval((x0+20, y0+20), (x1-20, y1 -20), fill= coul[i])
    

root.mainloop()
