import cv2
import numpy as np
import matplotlib.pyplot as plt
#Filtro que elimina las altas frecuencias, suavizan las imagenes
def pasa_bajas(imagen, frecuencia_corte):
    canales_filtrados = []
    for canal in cv2.split(imagen):
        # Transformada de Fourier 2D
        dft = np.fft.fft2(canal)
        # Desplazamiento del cero de frecuencia al centro del espectro
        dft_shift = np.fft.fftshift(dft)

        # Crear una máscara de paso bajo
        filas, columnas = canal.shape
        centro_filas, centro_columnas = filas // 2, columnas // 2
        mascara = np.zeros((filas, columnas), np.uint8)
        radio = int(min(filas, columnas) * frecuencia_corte)
        cv2.circle(mascara, (centro_columnas, centro_filas), radio, 1, thickness=-1)

        # Aplicar la máscara al DFT
        dft_shift_filtrado = dft_shift * mascara
        # Deshacer el desplazamiento del cero de frecuencia
        dft_filtrado = np.fft.ifftshift(dft_shift_filtrado)
        # Transformada Inversa de Fourier 2D
        canal_filtrado = np.fft.ifft2(dft_filtrado)
        # Obtener la magnitud del resultado complejo
        canal_filtrado = np.abs(canal_filtrado)
        canales_filtrados.append(canal_filtrado)

    # Combinar los canales filtrados en una imagen
    imagen_filtrada = cv2.merge(canales_filtrados)
    return imagen_filtrada

#hace que se realce los bordes en las imagenes. 
def pasa_altas(imagen, frecuencia_corte):
    canales_filtrados = []
    for canal in cv2.split(imagen):
        # Transformada de Fourier 2D
        dft = np.fft.fft2(canal)
        # Desplazamiento del cero de frecuencia al centro del espectro
        dft_shift = np.fft.fftshift(dft)

        # Crear una máscara de paso alto (invertir la máscara de paso bajo)
        filas, columnas = canal.shape
        centro_filas, centro_columnas = filas // 2, columnas // 2
        mascara = np.ones((filas, columnas), np.uint8)
        radio = int(min(filas, columnas) * frecuencia_corte)
        cv2.circle(mascara, (centro_columnas, centro_filas), radio, 0, thickness=-1)

        # Aplicar la máscara al DFT
        dft_shift_filtrado = dft_shift * mascara
        # Deshacer el desplazamiento del cero de frecuencia
        dft_filtrado = np.fft.ifftshift(dft_shift_filtrado)
        # Transformada Inversa de Fourier 2D
        canal_filtrado = np.fft.ifft2(dft_filtrado)
        # Obtener la magnitud del resultado complejo
        canal_filtrado = np.abs(canal_filtrado)
        canales_filtrados.append(canal_filtrado)

    # Combinar los canales filtrados en una imagen
    imagen_filtrada = cv2.merge(canales_filtrados)
    return imagen_filtrada

# Cargar la imagen original en color
ruta_imagen = r'C:\Users\bhald\Downloads\Proyecto_Series_de_Fourier\img2.png'
imagen = cv2.imread(ruta_imagen)

#Iteracion de frecuencias. 
frecuencias_corte = [0.2, 0.1, 0.9]
imagenes_pasa_bajas = [pasa_bajas(imagen, f) for f in frecuencias_corte]
imagenes_pasa_altas = [pasa_altas(imagen, f) for f in frecuencias_corte]

plt.figure(figsize=(18, 12))

plt.subplot(3, 4, 1)
plt.title("Imagen Original")
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.axis("off")

for i, (imagen_filtrada, f) in enumerate(zip(imagenes_pasa_bajas, frecuencias_corte), start=2):
    plt.subplot(3, 4, i)
    plt.title(f"Filtro Pasa Bajas (corte = {f})")
    plt.imshow(cv2.cvtColor(imagen_filtrada.astype(np.uint8), cv2.COLOR_BGR2RGB))
    plt.axis("off")

for i, (imagen_filtrada, f) in enumerate(zip(imagenes_pasa_altas, frecuencias_corte), start=6):
    plt.subplot(3, 4, i + 4)
    plt.title(f"Filtro Pasa Altas (corte = {f})")
    plt.imshow(cv2.cvtColor(imagen_filtrada.astype(np.uint8), cv2.COLOR_BGR2RGB))
    plt.axis("off")

plt.tight_layout()
plt.show()
