import sqlite3
import socket
import pickle

host = socket.gethostname()
port = 5000
server_socket = socket.socket()
server_socket.bind((host, port)) 
server_socket.listen(2)
con1, address = server_socket.accept()

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM inventory")
results = cursor.fetchall()
l1=[0,0,0,0,0,0,0,0,0,0]
l2=[0,0,0,0,0,0,0,0,0,0]
l3=[0,0,0,0,0,0,0,0,0,0]
j=0
for i in results:
    l1[j]=(i[1])
    j+=1
j=0
for i in results:
    l2[j]=(i[2])
    j+=1
j=0
for i in results:
    l3[j]=(i[3])
    j+=1
print(l1)
print(l2)
print(l3)
print(l1)
l11=pickle.dumps(l1)
print(l2)
l22=pickle.dumps(l2)
print(l3)
l33=pickle.dumps(l3)
con1.send(l11)
con1.send(l22)
con1.send(l33)