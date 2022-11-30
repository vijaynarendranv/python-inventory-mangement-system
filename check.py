import sqlite3

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