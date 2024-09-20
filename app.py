from flask import Flask, request, render_template, redirect, url_for, flash
from app_blueprint import app_bp
from auto import Autos

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para flash messages y sesiones
app.register_blueprint(app_bp)

# Lista para almacenar los autos
autos_registrados = []

@app.route('/get', methods=['GET'])
def peticion():
    return "<h1>Hola mundo</h1>"

@app.route('/get/<id>', methods=['GET'])
def peticion2(id):
    return f"<p>El ID es: <strong>{id}</strong></p>"

@app.route('/post', methods=['POST'])
def peticion_post():
    nombre = request.json['nombre']
    return f"<p>El nombre es: <strong>{nombre}</strong></p>"

# Ruta para procesar el login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'empleado' and password == 'empleado':
        return redirect(url_for('autos'))
    else:
        flash('Usuario o contraseña incorrectos.')  # Mensaje flash para el error
        return render_template('login.html')  # Recargar la misma página de login





@app.route('/autos', methods=['GET', 'POST'])
def autos():
    if request.method == 'POST':
        try:
            id_tipo_auto = int(request.form['id'])
            marca = request.form['marca']
            modelo = request.form['modelo']
            descripcion = request.form['descripcion']
            precio = float(request.form['precio'])
            cantidad = int(request.form['cantidad'])
            imagen = request.form['imagen']

            # Verificar si el auto ya existe
            for auto in autos_registrados:
                if auto.idTipoAuto == id_tipo_auto:
                    flash('El auto con este ID ya está registrado.')
                    return render_template('autos.html', autos=autos_registrados)  # Mantener la lista

            # Agregar el nuevo auto si no existe
            nuevo_auto = Autos(id_tipo_auto, marca, modelo, descripcion, precio, cantidad, imagen)
            autos_registrados.append(nuevo_auto)
            flash('Auto registrado exitosamente.')

        except ValueError as e:
            flash(f'Error en los datos ingresados: {e}')  # Mensaje flash para el error

    return render_template('autos.html', autos=autos_registrados)



# Ruta para eliminar autos
@app.route('/autos/eliminar/<int:idTipoAuto>', methods=['POST'])
def eliminar_auto(idTipoAuto):
    global autos_registrados
    print(f"Lista antes de eliminar: {autos_registrados}")  # Verifica el estado
    autos_registrados = [auto for auto in autos_registrados if auto.idTipoAuto != idTipoAuto]
    print(f"Lista después de eliminar: {autos_registrados}")  # Verifica el estado
    flash('Auto eliminado correctamente.')
    return redirect(url_for('autos'))



if __name__ == '__main__':
    app.run(debug=True, port=5000)
