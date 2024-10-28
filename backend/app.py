from flask import Flask, jsonify, request, send_file, make_response # type: ignore
from flask_cors import CORS # type: ignore
from scipy.integrate import quad # type: ignore
import numpy as np # type: ignore
from numpy import pi, sin, cos, tan, arcsin, arccos, arctan, log, e # type: ignore
import matplotlib # type: ignore
matplotlib.use('Agg') # type: ignore
import matplotlib.pyplot as plt # type: ignore
import io
import base64
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

def periodo(a, b):
    return b - a

def extension_periodica(a, b):
  T = periodo(a, b)

  return lambda f: lambda t: f((t - a) % T + a)

def fourier_a0(f, T):
    a0 = (1 / T) * quad(f, 0, T)[0]
    
    return a0

def fourier_an(f, T, n):
    W = (2 * np.pi) / T
    integrando = lambda t: f(t) * np.cos(n * W * t)
    an = (2 / T) * quad(integrando, 0, T)[0]

    return an

def fourier_bn(f, T, n):
    W = (2 * np.pi) / T
    integrando = lambda t: f(t) * np.sin(n * W * t)
    bn = (2 / T) * quad(integrando, 0, T)[0]

    return bn

def fourier_series(f, T, N):
    a0 = fourier_a0(f, T)
    an = [fourier_an(f, T, n) for n in range(1, N + 1)]
    bn = [fourier_bn(f, T, n) for n in range(1, N + 1)]

    return a0, an, bn

def fourier_approximation(f, T, N):
    a0, an, bn = fourier_series(f, T, N)
    W = (2 * np.pi) / T

    S = lambda t: a0 + sum([(an[n - 1] * np.cos(n * W * t)) + (bn[n - 1] * np.sin(n * W * t)) for n in range(1, N + 1)])

    return S

def graficar(t, f):
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize = (15, 5))
    plt.axes()
    plt.plot(t, np.vectorize(f)(t))
    plt.title("Serie de Fourier Trigonométrica Truncada a 2N + 1")
    plt.xlabel("t")
    plt.ylabel("f(t)")

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return img_base64

def Ef(f, T):
    integrando = lambda t: f(t)**2
    E_f = quad(integrando, 0, T)[0]

    return E_f
    
@app.route('/serie_fourier', methods=['POST'])
def main():
    data = request.get_json()
    nFunciones = int(data.get("nFunciones"))
    
    f1 = data.get("f1")
    r1_a = float(eval(data.get("r1_a")))
    r1_b = float(eval(data.get("r1_b")))

    N = 10
    
    if nFunciones == 1:
        @extension_periodica(r1_a, r1_b)
        def funcion1(t):
            if r1_a <= t <= r1_b:
                expresion = f1.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            else:
                return 0
            
        T = periodo(r1_a, r1_b)
        a0, an, bn = fourier_series(funcion1, T, N)
        valores_t = np.linspace(r1_a, r1_b, 1000)
        serie_fourier = fourier_approximation(funcion1, T, (2 * N) + 1)
        imagenGrafica = graficar(valores_t, serie_fourier)
            
    elif nFunciones == 2:
        f2 = data.get("f2")
        r2_a = float(eval(data.get("r2_a")))
        r2_b = float(eval(data.get("r2_b")))

        @extension_periodica(r1_a, r2_b)
        def funcion2(t):
            if r1_a <= t <= r1_b:
                expresion = f1.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            elif r2_a <= t <= r2_b:
                expresion = f2.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            else:
                return 0
        
        T = periodo(r1_a, r2_b)
        a0, an, bn = fourier_series(funcion2, T, N)
        valores_t = np.linspace(r1_a, r2_b, 1000)
        serie_fourier = fourier_approximation(funcion2, T, (2 * N) + 1)
        imagenGrafica = graficar(valores_t, serie_fourier)
        
    elif nFunciones == 3:
        f2 = data.get("f2")
        r2_a = float(eval(data.get("r2_a")))
        r2_b = float(eval(data.get("r2_b")))

        f3 = data.get("f3")
        r3_a = float(eval(data.get("r3_a")))
        r3_b = float(eval(data.get("r3_b")))

        @extension_periodica(r1_a, r3_b)
        def funcion3(t):
            if r1_a <= t <= r1_b:
                expresion = f1.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            elif r2_a <= t <= r2_b:
                expresion = f2.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            elif r3_a <= t <= r3_b:
                expresion = f3.replace("t", "(" + str(t) + ")")

                return float(eval(expresion))
            else:
                return 0
        
        T = periodo(r1_a, r3_b)
        valores_t = np.linspace(r1_a, r3_b, 1000)
        a0, an, bn = fourier_series(funcion3, T, N)
        serie_fourier = fourier_approximation(funcion3, T, (2 * N) + 1)
        imagenGrafica = graficar(valores_t, serie_fourier)

    response = jsonify({
        "T": T,
        "a0": a0,
        "an": an,
        "bn": bn,
        "imagenGrafica": imagenGrafica,
        "N": N,
        "ecuacionSerieFourier": "",
    })
            
    return make_response(response)

if __name__ == '__main__':
    app.run(debug=True)