from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfile
import os

sk_root = Tk()
a=500
b=380
color ="cyan"
sk_root.geometry(f"{a}x{b}")
sk_root.title("Untitled - Note")
sk_root.configure(background=f"{color}")


#functions

def createfile():
    global file
    sk_root.title("Untitled - Note")
    file=None
    note.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file=None
    else :
        sk_root.title(os.path.basename(file) + " - Note")
        note.delete(1.0,END)
        f=open(file, "r")
        note.insert(1.0, f.read())
        f.close()

def exitfile():
    sk_root.destroy()

def savefile():
    global file
    if file==None:
        file=asksaveasfile(initialfile= 'Untitled.txt',defaultextension=".txt",
                           filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None

        else :
            f=open(file,"w")
            f.write(note.get(1.0,END))
            f.close()
            sk_root.title(os.path.basename(file) + " - Note")
            print("File saved successfully...")

    else :
        f = open(file, "w")
        f.write(note.get(1.0, END))
        f.close()


def cut():
    note.event_generate(("<<Cut>>"))
def copy():
    note.event_generate(("<<Copy>>"))
def paste():
    note.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo("Notepad...","Done by Sparsh Kumar...")


#sk_root.wm_iconbitmap("1.ico")

#According to ur need
style="lucida"
size=20
fashion="bold"

note = Text(sk_root,font =f"{style} {size} {fashion}")
file = None
note.pack(expand=True, fill=BOTH)


s=Menu(sk_root)
s1=Menu(s,tearoff=0)
s1.add_command(label="New",command= createfile)
s1.add_command(label="Open",command= openfile)
s1.add_command(label="Save",command= savefile)
s1.add_separator()
s1.add_command(label="Exit",command= exitfile)
s.add_cascade(label="File" , menu=s1)
s2 = Menu(s, tearoff=0)
s2.add_command(label="Cut", command=cut)
s2.add_command(label="Copy", command=copy)
s2.add_command(label="Paste", command=paste)
s.add_cascade(label="Edit", menu=s2)

s3=Menu(s,tearoff=0)
s3.add_command(label="About", command=about)
s.add_cascade(label="Help", menu=s3)
sk_root.config(menu=s)

#Scrolling code
sb=Scrollbar(note)
sb.pack(side=RIGHT, fill=Y, pady= 7, padx=8)
sb.config(command= note.yview)
note.config(yscrollcommand=sb.set)

sk_root.mainloop()