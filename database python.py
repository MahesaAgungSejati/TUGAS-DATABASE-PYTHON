#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


# In[2]:


import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd =""
)

#preparing a cursor
cursorObject = database.cursor()

#creating databse
cursorObject.execute("CREATE DATABASE d3ti2023")


# In[12]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

#creating table
studentRecord ="""CREATE TABLE Mahasiswa(
             NIM VARCHAR(10) NOT NULL,
             NAME VARCHAR(30)NOT NULL,
             ALAMAT VARCHAR(255),
             MATKUL VARCHAR(10)
             )"""


# table created
cursorObject.execute(studentRecord)

# disconnecting from server
database.close()


# In[14]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

#creating table
studentRecord ="""CREATE TABLE Dosen(
             NIP VARCHAR(20) NOT NULL,
             NAME_DOSEN VARCHAR(50) NOT NULL,
             MATKUL VARCHAR(50)
             )"""


# table created
cursorObject.execute(studentRecord)

# disconnecting from server
database.close()


# In[15]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

#creating table
studentRecord ="""CREATE TABLE MATA_KULIAH(
             KODE_MATKUL VARCHAR(10) NOT NULL,
             NAMA_MATKUL VARCHAR(50)NOT NULL,
             WAKTU DATE,
             RUANGAN VARCHAR(10)
             )"""


# table created
cursorObject.execute(studentRecord)

# disconnecting from server
database.close()


# In[16]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

sql = "INSERT INTO Mahasiswa (NIM, NAME, ALAMAT, MATKUL)VALUES (%s, %s, %s, %s)"
val = [("V3922029", "Mahesa", "Madiun", "PBO"),
      ("V3922030", "Farhan", "jambi", "APSI"),
      ("V3922031", "Bayu", "Mojokerjo", "WIRELESS"),
      ("V3922032", "Brian", "Magetan", "KWU"),
      ("V3922033", "Budi", "Jombang", "PRAKWEB"),
      ("V3922034", "Bagas", "Papua", "BASIS DATA")
      
      ]

cursorObject.executemany(sql, val)
database.commit()


# In[17]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

sql = "INSERT INTO Dosen (NIP, NAME_DOSEN, MATKUL)VALUES (%s, %s, %s)"
val = [("888999111", "Santoso", "PBO"),
      ("888999112", "Suryo", "APSI"),
      ("888999113", "Mikel", "WIRELESS"),
      ("888999114", "Suwardi", "KWU"),
      ("888999115", "Murjianto", "PRAKWEB"),
      ("888999116", "Joko", "BASIS DATA")
      
      ]

cursorObject.executemany(sql, val)
database.commit()


# In[20]:


import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = '',
  database= "d3ti2023"
)

#preparing a cursor object
cursorObject = database.cursor()

sql = "INSERT INTO MATA_KULIAH (KODE_MATKUL, NAMA_MATKUL, WAKTU, RUANGAN)VALUES (%s, %s, %s, %s)"
val = [("111222", "PBO", "2023-01-01", "LAB 1"),
      ("111333", "APSI", "2023-01-02", "LAP 2"),
      ("111444", "WIRELESS", "2023-01-03", "LAB 3"),
      ("111555", "KWU", "2023-01-04", "LAB 4"),
      ("111666", "PRAKWEB", "2023-01-05", "LAB 5"),
      ("111777", "BASIS DATA", "2023-01-06", "LAB 6")
      
      ]

cursorObject.executemany(sql, val)
database.commit()


# In[22]:


import mysql.connector

database = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = '',
    database = 'd3ti2023'
)

# preparing cursor
cursorObject = database.cursor()

sql = "SELECT KODE_MATKUL, NAMA_MATKUL, NIM, NAME, NAME_DOSEN        FROM MATA_KULIAH        JOIN Mahasiswa ON KODE_MATKUL = KODE_MATKUL        JOIN Dosen ON KODE_MATKUL = KODE_MATKUL"

cursorObject.execute(sql)
result = cursorObject.fetchall()

for row in result:
    print(row)


# In[ ]:




