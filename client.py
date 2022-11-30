from tkinter import *
from tkinter import ttk
import socket
import sqlite3
import pickle

dec1=[]
dec2=[]

host = "169.254.30.3"
port = 35000
client_socket = socket.socket()
client_socket.connect((host, port))
uid=1001

l11=client_socket.recv(1024)
l22=client_socket.recv(1024)                    
l1=pickle.loads(l11)                           
l2=pickle.loads(l22)
l3=[100,100,100,100,100,100,100,100,100,100,100]  

def print():
    dec11=pickle.dumps(dec1)
    dec22=pickle.dumps(dec2)
    client_socket.send(dec11)
    client_socket.send(dec22)
    tott = float(totText.get())
    top = Toplevel()
    top.geometry("300x300")
    top.config(bg="white")
    l = Label(top, text='---------RECIEPT----------')
    l.pack()
    l.config(bg="white")
    dec11=pickle.dumps(dec1)
    dec22=pickle.dumps(dec2)
    client_socket.send(dec11)
    client_socket.send(dec22)
    heading = Label(top, text='\tItem\tPRICE\tQTY\tTOTAL')
    heading.pack()
    heading.config(bg="white")
 
    for child in listBox.get_children():
        item = (listBox.item(child, 'values')[0])
        price = float(listBox.item(child, 'values')[1])
        qty = float(listBox.item(child, 'values')[2])
        tot = float(listBox.item(child, 'values')[3])
        item1 = Label(top, text=f'{item}\t{price}\t{qty}\t{tot}')
        item1.config(bg="white")
        item1.pack()
 
    tot = Label(top, text=f'Total\t{tott}')
    tot.config(bg="white")
    tot.pack()
 
 
def show():
    tot = 0
    if (var1.get()):
        price = int(l2[0])
        qty = int(e1.get())
        tot = int(price * qty)
        tempList = [[l1[0], price , qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[0])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var2.get()):
        price = int(l2[1])
        qty = int(e2.get())
        tot = int(price * qty)
        tempList = [[l1[1], price , qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[1])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var3.get()):
        price = int(l2[2])
        qty = int(e3.get())
        tot = int(price * qty)
        tempList = [[l1[2], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[2])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var4.get()):
        price = int(l2[3])
        qty = int(e4.get())
        tot = int(price * qty)
        tempList = [[l1[4], price , qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[3])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    if (var5.get()):
        price = int(l2[4])
        qty = int(e5.get())
        tot = int(price * qty)
        tempList = [[l1[4], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[4])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var6.get()):
        price = int(l2[5])
        qty = int(e6.get())
        tot = int(price * qty)
        tempList = [[l1[5], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[5])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
    
    if (var7.get()):
        price = int(l2[6])
        qty = int(e7.get())
        tot = int(price * qty)
        tempList = [[l1[6], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[6])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
    
    if (var8.get()):
        price = int(l2[7])
        qty = int(e8.get())
        tot = int(price * qty)
        tempList = [[l1[7], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[7])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
    
    if (var9.get()):
        price = int(l2[8])
        qty = int(e9.get())
        tot = int(price * qty)
        tempList = [[l1[8], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[8])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))

    if (var10.get()):
        price = int(l2[9])
        qty = int(e10.get())
        tot = int(price * qty)
        tempList = [[l1[9], price, qty , tot]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        dec1.append(l1[9])
        dec2.append(qty)
        for i, (item, price, qty, tot) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(item, price, qty, tot))
 
    sum1 = 0.0
    for child in listBox.get_children():
        sum1 += float(listBox.item(child, 'values')[3])
    totText.set(sum1)
 
 
root = Tk()
root.title("Inventory Management System - Client")
root.geometry("1000x600")
global e1
global e2
global e3
global e4
global totText
global balText
 
totText = StringVar()
balText = IntVar()
 
Label(root, text="Inventory Management System-Server", font="arial 22 bold" ,bg="white").place(x=5, y=10)

conn = sqlite3.connect("data.db")
cursor = conn.cursor()


results = cursor.fetchall()
j=0
for i in results:
    l1[j]=i[1]
    j+=1
j=0
for i in results:
    l2[j]=i[2]
    j+=1
j=0
for i in results:
    l3[j]=i[3]
    j+=1
dem=0
k=0
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()

prc1=IntVar()
prc2=IntVar()
prc3=IntVar()
prc4=IntVar()
prc5=IntVar()
prc6=IntVar()
prc7=IntVar()
prc8=IntVar()
prc9=IntVar()
prc10=IntVar()

qty1=Entry(root)
qty2=Entry(root)
qty3=Entry(root)
qty4=Entry(root)
qty5=Entry(root)
qty6=Entry(root)
qty7=Entry(root)
qty8=Entry(root)
qty9=Entry(root)
qty10=Entry(root)



var1 = IntVar()
Checkbutton(root, text=l1[0], variable=var1).place(x=10, y=50)
pricebt1=Button(root,text=l2[0]).place(x=140,y=50)
qtybtn1=Button(root,text=l3[0]).place(x=300,y=50)
e1= Entry(root)
e1.place(x=400,y=50)

var2 = IntVar()
Checkbutton(root, text=l1[1], variable=var2).place(x=10, y=80)
pricebt2=Button(root,text=l2[1]).place(x=140,y=80)
qtybtn2=Button(root,text=l3[1]).place(x=300,y=80)
e2= Entry(root)
e2.place(x=400,y=80)

var3 = IntVar()
Checkbutton(root, text=l1[2], variable=var3).place(x=10, y=110)
pricebt3=Button(root,text=l2[2]).place(x=140,y=110)
qtybtn3=Button(root,text=l3[2]).place(x=300,y=110)
e3= Entry(root)
e3.place(x=400,y=110)

var4 = IntVar()
Checkbutton(root, text=l1[3], variable=var4).place(x=10, y=140)
pricebt4=Button(root,text=l2[3]).place(x=140,y=140)
qtybtn4=Button(root,text=l3[3]).place(x=300,y=140)
e4= Entry(root)
e4.place(x=400,y=140)

var5 = IntVar()
Checkbutton(root, text=l1[4], variable=var5).place(x=10, y=170)
pricebt5=Button(root,text=l2[4]).place(x=140,y=170)
qtybtn5=Button(root,text=l3[4]).place(x=300,y=170)
e5= Entry(root)
e5.place(x=400,y=170)

var6 = IntVar()
Checkbutton(root, text=l1[5], variable=var6).place(x=10, y=200)
pricebt6=Button(root,text=l2[5]).place(x=140,y=200)
qtybtn6=Button(root,text=l3[5]).place(x=300,y=200)
e6= Entry(root)
e6.place(x=400,y=200)

var7 = IntVar()
Checkbutton(root, text=l1[6], variable=var7).place(x=10, y=230)
pricebt7=Button(root,text=l2[6]).place(x=140,y=230)
qtybtn7=Button(root,text=l3[6]).place(x=300,y=230)
e7= Entry(root)
e7.place(x=400,y=230)

var8 = IntVar()
Checkbutton(root, text=l1[7], variable=var8).place(x=10, y=260)
pricebt8=Button(root,text=l2[7]).place(x=140,y=260)
qtybtn8=Button(root,text=l3[7]).place(x=300,y=260)
e8= Entry(root)
e8.place(x=400,y=260)

var9 = IntVar()
Checkbutton(root, text=l1[8], variable=var9).place(x=10, y=290)
pricebt9=Button(root,text=l2[8]).place(x=140,y=290)
qtybtn9=Button(root,text=l3[8]).place(x=300,y=290)
e9= Entry(root)
e9.place(x=400,y=290)

var10 = IntVar()
Checkbutton(root, text=l1[9], variable=var10).place(x=10, y=320)
pricebt10=Button(root,text=l2[9]).place(x=140,y=320)
qtybtn10=Button(root,text=l3[9]).place(x=300,y=320)
e10= Entry(root)
e10.place(x=400,y=320)

Label(root, text="Total").place(x=600, y=10)
 
tot = Label(root, text="", font="arial 22 bold", textvariable=totText)
tot.place(x=650, y=10)
 
Button(root, text="Add", command=show, height=3, width=13).place(x=10, y=380)
 
Button(root, text="Print", command=print, height=3, width=13).place(x=850, y=120)
cols = ('item', 'price', 'qty', 'total')
listBox = ttk.Treeview(root, columns=cols, show='headings')
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=450)
 
root.mainloop()
