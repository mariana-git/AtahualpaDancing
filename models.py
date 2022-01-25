import sqlite3 as sql
import os

BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "/db/contactos.db")

con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
cur = con.cursor()

def insertUser(username,password):
	con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
	cur = con.cursor()
	cur.execute("INSERT INTO Usuarios (username,password) VALUES (?,?)", (username,password))
	con.commit()
	con.close()

def retrieveContacts():	
	con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
	cur = con.cursor()
	cur.execute("SELECT * FROM Contactos")
	users = cur.fetchall()
	con.close()
	return users