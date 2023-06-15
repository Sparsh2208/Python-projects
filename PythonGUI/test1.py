from tkinter import *
import tkinter.messagebox as tmsg
sk_root = Tk()
sk_root.geometry("1300x800")
sk_root.title("SK GUI test series.....")
sk_root.minsize(1000,750)
sk_root.maxsize(1500,1300)
sk_root.configure(background="cyan")
def add() :
    print("sum is ...")
def minus() :
    print("Subtraction is......")
def savefarzi() :
    print("save nhi krna abhi bad m dekhenge.....")
def d1() :
    tmsg.showinfo("SK loved it....","Rain in November........")
#photo = PhotoImage(file=""C:\Users\spars\PycharmProjects\pythonProject\peter-broomfield-m3m-lnR90uM-unsplash.png"")
sk_label=Label(text="Sparsh is legend\n In this calculator you can perform 100 functions directly using its interface \n Lets do it.....\n",bg="red",fg="blue",padx=10,pady=15,font="comicsansms 12 italic",borderwidth=5,relief="sunken")
sk_label.pack(fill=X,padx=15,pady=25)
f1=Frame(sk_root,bg="green",relief=SUNKEN)
f1.pack(side=LEFT,fill="y",anchor="nw")
b1=Button(f1,text="Sparsh",command=add,bg="black",fg="white",borderwidth=3)
b1.pack(side=TOP,)
f1_label=Label(f1,text="1...",padx=10,pady=15)
f1_label.pack(pady=15,padx=10,fill="x")
f2=Frame(sk_root,borderwidth=5,bg="green",relief=SUNKEN)
f2.pack(side=TOP,fill="x")
f2_label=Label(f2,text="2...",padx=10,pady=15)
f2_label.pack(pady=15,padx=10,fill="x")
b2=Button(f2,text="Sparsh 2",bg="yellow",fg="blue",command=minus,borderwidth=3)
b2.pack(side=RIGHT,padx=10,pady=15)
#menusir=Menu(sk_root)
#menusir.add_command(label="Exit",command=quit())
#sk_root.config(menu=menusir)

s=Menu(sk_root,tearoff=0)
s1=Menu(s)
s1.add_command(label="Save",command=savefarzi)
s1.add_command(label="Car Love",command=savefarzi)
s1.add_command(label="Champion...",command=savefarzi)
s1.add_command(label="S.K.",command=savefarzi)
s2=Menu(s)
s2.add_command(label="Hi")
s3=Menu(s)
s3.add_command(label="tests1",command=d1)
#s1.add_command(label="exit",command=quit())
sk_root.config(menu=s)
s.add_cascade(label="File", menu=s1)
s.add_cascade(label="Sparsh", menu=s2)
s.add_cascade(label="Duniyaa", menu=s3)

Scale(sk_root,from_=0,to=100,tickinterval=25).pack()



sb=Scrollbar(sk_root)
sb.pack()
lbx=Listbox(sk_root,yscrollcommand=sb.set)
lbx.insert(END,"Hi")
lbx.pack()
sb.config(command=lbx.xview())

statusbar = StringVar()
statusbar.set("Ready Sir....")
sbar=Label(sk_root,textvariable=statusbar,relief=GROOVE,anchor=W)
sbar.pack( side=BOTTOM)








sk_root=mainloop()
