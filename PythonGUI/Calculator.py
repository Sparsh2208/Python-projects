from tkinter import *
import math
import tkinter.messagebox as tmsg


#Defining functions used in the calc

def click(event):
    global screen
    text=event.widget.cget("text")
    print(text)

    if text == "=":
        if screen.get().isdigit() :
            value =  int(screen.get())
        else :
            try:
                value = eval(screen.get())
            except Exception as e:
                screen.set("Error....")
                svalue.update()

        screen.set(value)
        svalue.update()

    elif text == "C":
        screen.set("")
        svalue.update()


    else:
       screen.set(screen.get() + text)
       svalue.update()


sk_root = Tk()
a=700
b=500
sk_root.geometry(f"{a}x{b}")
sk_root.title("Calc by SK")
sk_root.configure(background="cyan")



#For top screen or for display.........
screen = StringVar()
screen.set("")
svalue=Entry(sk_root, textvar=screen, font="lucida 40 italic")
svalue.pack(side=TOP,fill=X, padx=8, pady=12, ipadx=10, ipady=15)

#Framing including buttons
style="lucida"
size=20
fashion="bold"

f1=Frame(sk_root,bg="red",relief=SUNKEN)

b1=Button(f1, text="7", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="8", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="9", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="+", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)


f1.pack(fill="y")

f1=Frame(sk_root,bg="red",relief=SUNKEN)

b1=Button(f1,text="4", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="5", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="6", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="-", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)


f1.pack(fill="y")


f1=Frame(sk_root,bg="red",relief=SUNKEN)

b1=Button(f1,text="1", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="2", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="3", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="/", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)


f1.pack(fill="y")

f1=Frame(sk_root,bg="red",relief=SUNKEN)

b1=Button(f1,text="**", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="0", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="C", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)

b1=Button(f1,text="=", font=f"{style} {size} {fashion}" ,bg="white",fg="blue",borderwidth=4, padx=10, pady=12)
b1.pack(side=LEFT,padx=8, pady=10)
b1.bind("<Button-1>",click)


f1.pack(fill="y")





sk_root.mainloop()
