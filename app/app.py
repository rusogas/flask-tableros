from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import random
from flask import Response

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el primer tablero (gráfico de torta)
@app.route('/tablero1')
def tablero1():
    # Generar datos aleatorios para el gráfico
    labels = ['A', 'B', 'C', 'D']
    sizes = [random.randint(10, 40) for _ in range(4)]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    # Crear el gráfico de torta
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    # Guardar el gráfico en un objeto BytesIO y retornarlo como imagen
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return Response(img.getvalue(), mimetype='image/png')

# Ruta para el segundo tablero (gráfico de torta)
@app.route('/tablero2')
def tablero2():
    labels = ['W', 'X', 'Y', 'Z']
    sizes = [random.randint(10, 40) for _ in range(4)]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return Response(img.getvalue(), mimetype='image/png')

# Ruta para el tercer tablero (gráfico de torta)
@app.route('/tablero3')
def tablero3():
    labels = ['L', 'M', 'N', 'O']
    sizes = [random.randint(10, 40) for _ in range(4)]
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return Response(img.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
