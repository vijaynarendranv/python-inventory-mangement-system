import socket
import pandas as pd
import pickle
import sqlite3

l1=[0,0,0,0,0,0,0,0,0,0]
l2=[0,0,0,0,0,0,0,0,0,0]
l3=[0,0,0,0,0,0,0,0,0,0]

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM inventory")
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

print(l1)
print(l2)
print(l3)
host =  "192.168.189.198"
port = 35000
server_socket = socket.socket()
server_socket.bind((host, port)) 
server_socket.listen(2)
con1, address = server_socket.accept()
print(l1)
l11=pickle.dumps(l1)
print(l2)
l22=pickle.dumps(l2)
print(l3)
l33=pickle.dumps(l3)
con1.send(l11)
print("")
con1.send(l22)
print("")
con1.send(l33)
item_name=con1.recv(1024)
item_name=pickle.loads(item_name)
item_qty=con1.recv(1024)
item_qty=pickle.loads(item_qty)
print(item_name)
print(item_qty)
for i,j in zip(item_name,item_qty):
    cursor.execute("UPDATE inventory SET itemQuantity = '" + str((100-int(j))) + "' WHERE itemName='"+str(i)+"'")
cursor.execute("SELECT * FROM inventory")
results = cursor.fetchall()
print(results)