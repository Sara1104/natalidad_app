from flask import Flask, render_template, request
from modelo import entrenar_modelo, predecir
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
modelo, datos = entrenar_modelo()

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    anio = None

    if request.method == "POST":
        anio = int(request.form["anio"])
        resultado = predecir(modelo, anio)
        graficar(modelo, datos, anio, resultado)

    return render_template("index.html", resultado=resultado, anio=anio)

def graficar(modelo, datos, anio, resultado):
    X = datos[['ANO']]
    y = datos['TOTAL_NACIDOS']
    prediccion = modelo.predict(X)

    plt.figure(figsize=(10,6))
    plt.scatter(X, y, color='blue', label='Datos reales')
    plt.plot(X, prediccion, color='red', label='Regresión')
    plt.scatter(anio, resultado, color='green', label=f'Predicción {anio}', s=100)
    plt.xlabel("Año")
    plt.ylabel("Total nacimientos")
    plt.title("Predicción de natalidad en Bogotá")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    if not os.path.exists("static"):
        os.makedirs("static")
    plt.savefig("static/prediccion.png")
    plt.close()

if __name__ == "__main__":
    app.run(debug=True)
