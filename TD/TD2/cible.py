import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1, column=1)


coul = [ "blue", "green","black", "yellow","magenta", "red", "blue", "green","black", "yellow","magenta", "red"]
def cercle(n,x0,y0,x1,y1,r):
    for i in range (n):
        canvas.create_oval((x0+r, y0+r), (x1-r, y1-r), fill=coul[i]) 
        r=r+20

cercle(6, -20,-20,520,520,20)

root.mainloop()





