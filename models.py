import sqlite3 as sql
import os

BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "/db/contactos.db")

con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
cur = con.cursor()

def insertComents(name,cel,mail,message):
	msg=""
	try:
		cur.execute("INSERT INTO Contactos (Nombre, Celular, Mail, Mensaje) VALUES ('{n}',{p},'{m}','{ms}');".format(n=name,p=cel,m=mail,ms=message))
		con.commit()
		con.close()
		msg="Gracias por comunicarte con nosotros"
	except sql.Error as e:
		con.rollback()  
		msg= "No pudimos Guardar Tu Consulta... Podrías Volver a Intentarlo?"
	finally:
		con.close()
	return msg

def loginUser(username,password):
	con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
	cur = con.cursor()
	cur.execute("SELECT * FROM Usuarios WHERE username ='{u}' AND password = '{p}';".format(u=username, p=password))
	exist = cur.fetchone()
	con.close()
	return exist

def retrieveContacts():	
	con = sql.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
	cur = con.cursor()
	#cur.execute("SELECT strftime('%d-%m-%Y',Fecha) as Fecha,Nombre,Celular,Mail,Mensaje FROM Contactos ORDER BY Fecha DESC;")
	cur.execute("SELECT * FROM Contactos ORDER BY Fecha DESC;")
	contacts = cur.fetchall()
	con.close()
	return contacts