from flask import Flask, render_template,request,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="localhost" ,user="root", password="rahulgurme18", database="register")
cursor = conn.cursor()

app.config['SECRET_KEY'] = '10125a01c112ff70f1232b9f9a2dc582'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:rahulgurme18@localhost/register'
db = SQLAlchemy(app)


class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

@app.route("/")
def Home():
    return  render_template("index.html")

@app.route("/home")
def hello():
    return redirect(url_for('Home'))

@app.route("/users", methods = ['GET','POST'])
def register():
    if(request.method=='POST'):
        email = request.form.get('email')
        password = request.form.get('psw')

        entry = Users(email=email,password=password)
        db.session.add(entry)
        db.session.commit()
        flash(f'Your Account has been created!', 'success')
        return redirect(url_for('ceaser'))

    return render_template("register.html")

@app.route("/login", methods = ['POST','GET'])
def login():

    email = request.form.get('email')
    password = request.form.get('psw')
    cursor.execute("""SELECT * FROM USERS WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email,password))
    users = cursor.fetchall()

    if len(users)>0:
        return redirect(url_for('ceaser'))
    else:
        return render_template('login.html')

@app.route("/ceaser-cipher")
def ceaser():
    return render_template("ceaser-cipher.html")

@app.route("/rail-fence")
def rail():
    return render_template("rail-fence.html")

@app.route("/play-fair")
def fair():
    return  render_template("play-fair.html")



app.run(debug=True)





