
from flask import Flask, render_template, request
import numpy as np
import math

app = Flask(__name__)

def generar_matriz(filas, columnas):
    return np.random.randint(1, 20, size=(filas, columnas))

def es_simetrica(m):
    return np.array_equal(m, m.T)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = {}
    if request.method == "POST":
        m1 = int(request.form["m1"])
        n1 = int(request.form["n1"])
        m2 = int(request.form["m2"])
        n2 = int(request.form["n2"])

        A = generar_matriz(m1, n1)
        B = generar_matriz(m2, n2)

        resultado["A"] = A
        resultado["B"] = B

        if m1 == m2 and n1 == n2:
            resultado["suma"] = 3 * A + 4 * B
            with np.errstate(invalid='ignore'):
                resultado["resta"] = A - np.sqrt(B)

        if n1 == m2:
            log_B = np.log10(B, where=B>0)
            resultado["multiplicacion"] = 2 * A @ log_B

            cubo_A = np.power(A, 3)
            sqrt_B = np.sqrt(B)
            resultado["cubo_sqrt"] = cubo_A @ sqrt_B

        if m1 == n1 and m2 == n2:
            resultado["sim_A"] = es_simetrica(A)
            resultado["sim_B"] = es_simetrica(B)

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
