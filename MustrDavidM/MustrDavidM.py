from tkinter import *
from tkinter import font
from random import * 

raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=1600, height=600, background="white")
tahvel.grid()

# функция для создания Эстонского флага
def estonian():
    # Eesti lipp
    tahvel.delete("all")
    tahvel.create_line(30, 40, 300, 40, width=50, fill="blue")
    tahvel.create_line(30, 80, 300, 80, width=50, fill="black")
    tahvel.create_line(30, 120, 300, 120, width=50, fill="white")
    tahvel.create_line(30, 15, 300, 15, 300, 135, 30, 135, 30, 15)
    tahvel.create_line(30, 100, 30, 100, width=1, fill="black")

# функция для создания флага Багамских Островов
def bahama():
    # Bahama lipp
    tahvel.delete("all")
    tahvel.create_line(30, 190, 300, 190, width=50, fill="teal")
    tahvel.create_line(30, 240, 300, 240, width=50, fill="yellow")
    tahvel.create_line(30, 280, 300, 280, width=50, fill="teal")
    tahvel.create_polygon(30, 165, 120, 235, 30, 305, fill="black")

def germany():
    # Germany
    tahvel.delete("all")
    tahvel.create_line(30, 250, 300, 250, width=50, fill="black")
    tahvel.create_line(30, 300, 300, 300, width=50, fill="red")
    tahvel.create_line(30, 340, 300, 340, width=50, fill="yellow")

def oval():
    tahvel.delete("all")
    colors=["black","cyan","magenta","red","blue","gray","yellow","green","lightblue","pink","gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=2
    for i in range(160):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        j=randrange(1,11)
        tahvel.create_oval(x0,y0,x1,y1, fill=colors[j])

def chess():
    tahvel.delete("all")
    chess=Canvas(raam, width=400/2, height=400/2, background="white")
    chess.grid(row=0,column=2,sticky=NW)
    chess.create_rectangle(0,0,400/2,400/2,fill="white")
    s1=400/2/8
    for x in range(8):
        for y in range(8):
            if (x+y)%2 == 0:
                chess.create_rectangle(x*s1,y*s1,(x+1)*s1,(y+1)*s1, fill="black")

def muster():
    tahvel.delete("all")
    muster = Canvas(raam, width=300, height=300, background="yellow")
    muster.grid()
    x0=0
    y0=0
    x1=300
    y1=300
    p=0
    x_=300
    y_=300
    for i in range(300):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
        muster.create_rectangle(x0,y0,x1,y1,fill="red")
        muster.create_oval(x0,y0,x1,y1,fill="blue")
        x_-=2*p
        y_-=2*p
        p=int(((x_**2+y_**2)**(1/2)-x_)/2)
        p=int(((p**2)/2)**(1/2))

def valgusfoorZ():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310, width=5, fill="black")
    tahvel.create_line(300, 500, 300, 310, width=50, fill="grey")
    tahvel.create_line(280, 280, 320, 280, width=50, fill="grey")
    tahvel.create_line(280, 220, 320, 220, width=50, fill="grey")
    tahvel.create_line(280, 160, 320, 160, width=50, fill="green")
    tahvel.create_line(280, 500, 350, 500, width=15, fill="grey")
    pass

def valgusfoorS():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310, width=5, fill="black")
    tahvel.create_line(300, 500, 300, 310, width=50, fill="grey")
    tahvel.create_line(280, 280, 320, 280, width=50, fill="grey")
    tahvel.create_line(280, 220, 320, 220, width=50, fill="yellow")
    tahvel.create_line(280, 160, 320, 160, width=50, fill="grey")
    tahvel.create_line(280, 500, 350, 500, width=15, fill="grey")
    pass

def valgusfoorK():
    tahvel.delete("all")
    tahvel.create_line(300, 500, 300, 310, width=5, fill="black")
    tahvel.create_line(300, 500, 300, 310, width=50, fill="grey")
    tahvel.create_line(280, 280, 320, 280, width=50, fill="red")
    tahvel.create_line(280, 220, 320, 220, width=50, fill="grey")
    tahvel.create_line(280, 160, 320, 160, width=50, fill="grey")
    tahvel.create_line(280, 500, 350, 500, width=15, fill="grey")
    pass

nupp = Button(raam, text="Eesti lipp", font="Arial 20", height=3, width=15, relief=RAISED, command=estonian, bg="blue")
nupp2 = Button(raam, text="Bahama lipp", font="Arial 20", height=3, width=15, relief=RAISED, command=bahama, bg="teal")
nupp3 = Button(raam, text="Germany",
font="Arial 20", height=3, width=15, relief=RAISED, command=germany, bg="red")
nupp4 = Button(raam, text="Oval", font="Arial 20", height=3, width=15, relief=RAISED, command=oval, bg="lightblue")
nupp5 = Button(raam, text="Chess", font="Arial 20", height=3, width=15, relief=RAISED, command=chess, bg="yellow")
nupp6 = Button(raam, text="muster", font="Arial 20", height=3, width=15, relief=RAISED, command=muster, bg="pink")
nupp7 = Button(raam, text="valgusfoorZ", font="Arial 20", height=3, width=15, relief=RAISED, command=valgusfoorZ, bg="grey")
nupp8 = Button(raam, text="valgusfoorS", font="Arial 20", height=3, width=15, relief=RAISED, command=valgusfoorS, bg="grey")
nupp9 = Button(raam, text="valgusfoorK", font="Arial 20", height=3, width=15, relief=RAISED, command=valgusfoorK, bg="grey")

nupp.place(x=0, y=450)
nupp2.place(x=225, y=450)
nupp3.place(x=450, y=450)
nupp4.place(x=675, y=450)
nupp5.place(x=900, y=450)
nupp6.place(x=1100, y=450)
nupp7.place(x=1300, y=450)
nupp8.place(x=1300, y=350)
nupp9.place(x=1300, y=250)


raam.mainloop()

