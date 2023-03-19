import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 540, height = 540, bg = "dark turquoise")
canvas.grid(row=1, column=1)


coul = [ "blue", "green","black", "yellow","magenta", "red", "blue", "green","black", "yellow","magenta", "red","blue", "green","black"]
def cercle(n,x0,y0,x1,y1,r):
    for i in range (n):
        canvas.create_oval((x0+r, y0+r), (x1-r, y1-r), fill=coul[i]) 
        r=r+20

cercle(14, 0,0,540,540,0.1)

root.mainloop()





