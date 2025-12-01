from tkinter import *

# Create root window
root = Tk()
root.title("Smiley Face")

# Create canvas as a child to root window
c = Canvas(root, bg="skyblue", height=500, width=500)
c.pack()

# Draw face (outer circle)
face = c.create_oval(100, 100, 400, 400, fill="yellow", outline="black", width=4)

# Draw eyes (two small black circles)
left_eye = c.create_oval(170, 180, 210, 220, fill="black")
right_eye = c.create_oval(290, 180, 330, 220, fill="black")

# Draw smile (arc)
smile = c.create_arc(180, 220, 320, 350, start=0, extent=-180, style=ARC, width=5)

# Draw nose (small triangle)
nose = c.create_polygon(240, 220, 260, 220, 250, 260, fill="orange", outline="black")

# Add text
fnt = ('Comic Sans MS', 20, 'bold')
text = c.create_text(250, 50, text="Smiley Canvas 😊", font=fnt, fill="white")

# Wait for any events
root.mainloop()
