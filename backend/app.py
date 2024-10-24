from flask import Flask, jsonify, request, send_file # type: ignore
from flask_cors import CORS # type: ignore
from scipy.integrate import quad # type: ignore
import numpy as np # type: ignore
from numpy import pi, sin, cos, tan # type: ignore
# from numpy import pi, sin, cos, tan # type: ignore
import matplotlib.pyplot as plt # type: ignore
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)
CORS(app)

def periodo(a, b):
    return b - a

def extension_periodica(a, b):
  T = periodo(a, b)

  return lambda f: lambda x: f((x - a) % T + a)

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

    S = lambda t: (a0 / 2) + sum([(an[n - 1] * np.cos(n * W * t)) + (bn[n - 1] * np.sin(n * W * t)) for n in range(1, N + 1)])

    return S

def Ef(f, T):
    integrando = lambda t: f(t)**2
    E_f = quad(integrando, 0, T)[0]

    return E_f

def graficar(t, f):
    plt.style.use("seaborn-v0_8-whitegrid")
    figura = plt.figure(figsize = (15, 5)) #Crea una figura con tamaño de 15 * 5.
    axes = plt.axes()

    plt.plot(t, np.vectorize(f)(t)) # Se gráfica la función de onda cuadrada.
    plt.title("Función 1") #Coloca el titulo a la figura.
    plt.xlabel("t") #Coloca un titulo a cada uno de los ejes.
    plt.ylabel("f(t)")
    plt.show() #Muestra las gráficas en la figura.
    
@app.route('/fourier', methods=['POST'])
def main():
    data = request.get_json()
    nFunciones = float(data.get("nFunciones"))
    
    f1 = data.get("f1")
    r1_a = float(data.get("r1_a"))
    r1_b = float(data.get("r1_b"))

    N = 10
    
    if nFunciones == 1:
        @extension_periodica(r1_a, r1_b)
        def funcion1(t):
            if r1_a < t <= r1_b:
                return float(eval(f1.replace("t", str(t))))
            else:
                return 0
            
        T = periodo(r1_a, r1_b)
        a0, an, bn = fourier_series(funcion1, T, N)
        valores_t = np.linspace(r1_a, r1_b, 1000)
        serie_fourier = fourier_approximation(funcion1, T, (2 * N) + 1)
        graficar(valores_t, serie_fourier)
            
    elif nFunciones == 2:
        f2 = data.get("f2")
        r2_a = float(data.get("r2_a"))
        r2_b = float(data.get("r2_b"))

        @extension_periodica(r1_a, r2_b)
        def funcion2(t):
            if r1_a < t <= r1_b:
                return float(eval(f1.replace("t", str(t))))
            elif r2_a < t <= r2_b:
                return float(eval(f2.replace("t", str(t))))
            else:
                return 0
        
        T = periodo(r1_a, r2_b)
        a0, an, bn = fourier_series(funcion2, T, N)
        valores_t = np.linspace(r1_a, r2_b, 1000)
        serie_fourier = fourier_approximation(funcion2, T, (2 * N) + 1)
        graficar(valores_t, serie_fourier)
        
    elif nFunciones == 3:
        f2 = data.get("f2")
        f3 = data.get("f3")
        r2_a = float(data.get("r2_a"))
        r2_b = float(data.get("r2_b"))

        r3_a = float(data.get("r3_a"))
        r3_b = float(data.get("r3_b"))

        @extension_periodica(r1_a, r3_b)
        def funcion3(t):
            if r1_a < t <= r1_b:
                return float(eval(f1.replace("t", str(t))))
            elif r2_a < t <= r2_b:
                return float(eval(f2.replace("t", str(t))))
            elif r3_a < t <= r3_b:
                return float(eval(f3.replace("t", str(t))))
            else:
                return 0
        
        T = periodo(r1_a, r3_b)
        a0, an, bn = fourier_series(funcion3, T, N)
        valores_t = np.linspace(r1_a, r3_b, 1000)
        serie_fourier = fourier_approximation(funcion3, T, (2 * N) + 1)
        graficar(valores_t, serie_fourier)

    response = {
        "T": T,
        "a0": a0,
        "an": an,
        "bn": bn
    }    
            
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)