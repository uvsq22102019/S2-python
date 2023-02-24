import tkinter as tk

root = tk.Tk()
root.title("Mon dessin")

canvas = tk.Canvas(root, width = 500, height = 500, bg = "black")
canvas.grid(row=1, column=1)

root.mainloop()