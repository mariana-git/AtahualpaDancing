from distutils.log import debug
from multiprocessing import connection
from sre_constants import SUCCESS
from flask import Flask, render_template,request, url_for,session
import models as dbHandler
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
    name = request.form["name"]
    cel = request.form["cel"]
    mail = request.form["mail"]
    message = request.form["message"]
    msg = dbHandler.insertComents(name,cel,mail,message)
    return render_template('result.html', msg = msg)
    

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/data', methods=['POST', 'GET'])
def data():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        exist = dbHandler.loginUser(username,password)
        if exist:           
            contacts = dbHandler.retrieveContacts()
            return render_template('data.html', contacts=contacts)
        else:
            msg = 'Login Incorrecto!'
            return render_template('login.html', msg = msg)
 

if __name__ ==  '__main__':
    app.run(debug=True)