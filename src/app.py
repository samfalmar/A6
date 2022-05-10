#Importamos el framework Flask
from flask import Flask, render_template, request, redirect, url_for, flash
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
    return redirect(url_for('login'))

#Definición de las rutas y los métodos GET / POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# Definimos el logout
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

# Definimos el home
@app.route('/home')
def home():
    return render_template('home.html')

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
