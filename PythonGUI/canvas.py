from tkinter import *
root=Tk()

cwidth=700
cheight=800

root.geometry(f"{cwidth}x{ cheight}")
cfx=Canvas(root,width=cwidth,height=cheight)
cfx.pack()
cfx.create_line(0,0,500,500)
cfx.create_line(0,500,500,0)
cfx.create_rectangle(10,0,500,500)




root.mainloop()