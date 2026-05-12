from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secreto"

usuarios = []

@app.route('/')
def inicio():
    return redirect('/login')

# ---------------- LOGIN ----------------

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        correo = request.form['correo']
        password = request.form['password']

        for usuario in usuarios:

            if usuario['correo'] == correo and usuario['password'] == password:

                session['usuario'] = usuario['nombre']

                return redirect('/dashboard')

    return render_template('login.html')

# ---------------- REGISTRO ----------------

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        password = request.form['password']

        usuarios.append({
            'nombre': nombre,
            'correo': correo,
            'password': password
        })

        return redirect('/login')

    return render_template('register.html')

# ---------------- DASHBOARD ----------------

@app.route('/dashboard')
def dashboard():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template('dashboard.html')

# ---------------- PROGRAMACION ----------------

@app.route('/programacion')
def programacion():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template('programacion.html')

# ---------------- SOPORTE ----------------

@app.route('/soporte')
def soporte():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template('soporte.html')

# ---------------- DISENO ----------------

@app.route('/diseno')
def diseno():

    if 'usuario' not in session:
        return redirect('/login')

    return render_template('diseno.html')

# ---------------- LOGOUT ----------------

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)