#Importamos el framework Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

#Cargamos el fichero de configuración config.py
from config import config

# Models
from models.Modeluser import ModelUser

# Entities
from models.entities.User import User

#Inicializamos la aplicación
app = Flask(__name__)

db = MySQL(app)


# Cuando accedemos a la ruta raíz nos redirigirá a login
@app.route('/')
def index():
    if not session.get("name"):
        return redirect(url_for('login'))
    return redirect(url_for('home'))

#Definición de las rutas y los métodos GET / POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get("name"):
        if request.method == 'POST':
            #print(request.form['username'])
            #print(request.form['password'])
            user = User(0, request.form['username'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            if logged_user != None:
                if logged_user.password:
                    session["name"] = request.form['username']
                    return redirect(url_for('home'))
                else:
                    flash("Invalid password...","alert-warning")
                    return render_template('auth/login.html')
            else:
                flash("User not found...","alert-warning")
                return render_template('auth/login.html')
        else:
            return render_template('auth/login.html')
    return redirect(url_for('home'))

#Definición de las rutas y los métodos GET / POST
@app.route('/register', methods=['GET', 'POST'])
def register():
    if not session.get("name"):
        if request.method == 'POST':
            user = User(0, request.form['username'], request.form['password'])
            logged_user = ModelUser.login(db, user)
            if logged_user != None:
                flash("El usuario ya existe","alert-warning")
                return render_template('auth/register.html')
            else:
                try:
                    cur = db.connection.cursor()
                    cur.execute("""INSERT INTO user (username, password) 
                            VALUES (%s, %s)""", (request.form['username'], User.hashed_password(request.form['password'])))
                    db.connection.commit()
                    cur.close()
                    flash("Usuario creado con éxito", "alert-success")
                    return redirect(url_for('login'))
                except Exception as ex:
                    raise Exception(ex)
        else:
            return render_template('auth/register.html')
    return redirect(url_for('home'))


# Definimos el logout
@app.route('/logout')
def logout():
    session["name"] = None
    return redirect(url_for('login'))

# Definimos el home
@app.route('/home')
def home():
    if not session.get("name"):
        return redirect(url_for('login'))
    return render_template('home.html', name = session['name'])

# Definimos el generate code
@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if session.get("name"):
        return render_template('generate.html', name = session['name'])
    return redirect(url_for('login'))   
    
    
@app.route('/vagrant',methods=['GET', 'POST'])
def vagrant():
    if session.get("name"):
        if request.method == 'POST':
            print(request.form['OS'])
            print(request.form['Cores'])
            print(request.form['Memory'])
            print(request.form['Hostname'])
            print(request.form['Network'])
            flash("Vagrantfile has been succesfuly created", "alert-success")
            return redirect(url_for('generate')) 
    return redirect(url_for('login'))          


# Definimos errores 401
def status_401(error):
    return redirect(url_for('login'))

# Definimos errores 404
def status_404(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
