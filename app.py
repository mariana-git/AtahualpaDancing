from distutils.log import debug
from multiprocessing import connection
from sre_constants import SUCCESS
from flask import Flask, render_template,request, url_for
import models as dbHandler
import sqlite3 
import os

BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "/db/contactos.db")

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/gallery")
def videos():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/result",methods = ["POST"])  
def result():
    msg = "msg"    
    connection = sqlite3.connect(BASE_DIR + "/db/contactos.db",check_same_thread=False)
    try:
        name = request.form["name"]
        cel = request.form["cel"]
        mail = request.form["mail"]
        message = request.form["message"]
        cursor = connection.cursor()
        query1 = "INSERT INTO Contactos (Nombre, Celular, Mail, Mensaje) VALUES ('{n}',{p},'{m}','{ms}');".format(n=name,p=cel,m=mail,ms=message)
        cursor.execute(query1)
        connection.commit()
        cursor.close()
        msg="Gracias por comunicarte con nosotros"
    except sqlite3.Error as e:
        connection.rollback()  
        msg= "No pudimos Guardar Tu Consulta... Podrías Volver a Intentarlo?"
    finally:
        connection.close()
        return render_template("result.html",msg = msg)

@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/data', methods=['POST', 'GET'])
def data():
        if request.method=='POST':        
                username = request.form['username']
                password = request.form['password']
                dbHandler.insertUser(username, password)
                users = dbHandler.retrieveContacts()
                return render_template('data.html', users=users)
        else:
                return render_template('index.html')
 

if __name__ ==  '__main__':
    app.run(debug=True)