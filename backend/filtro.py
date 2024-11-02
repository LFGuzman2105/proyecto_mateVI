import cv2
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import warnings
warnings.filterwarnings("ignore")

class ImageFilter:
    def __init__(self, image_path):
        self.image_path = image_path
        self.imagen = cv2.imread(image_path)
        if self.image is None:
            raise ValueError(f"No se pudo cargar la imagen desde la ruta: {image_path}")
    
    #Filtro que elimina las altas frecuencias, suavizan las imagenes
    def pasa_bajas(self, frec_corte):
        c_filtrados = []
        for canal in cv2.split(self.imagen):
            # Transformada de Fourier 2D
            dft = np.fft.fft2(canal)
            # Desplazamiento del cero de frecuencia al centro del espectro
            dft_shift = np.fft.fftshift(dft)

            # Crear una máscara de paso bajo
            filas, columnas = canal.shape
            centro_filas, centro_columnas = filas // 2, columnas // 2
            mascara = np.zeros((filas, columnas), np.uint8)
            radio = int(min(filas, columnas) * frec_corte)
            cv2.circle(mascara, (centro_columnas, centro_filas), radio, 1, thickness=-1)

            # Aplicar la máscara al DFT
            dft_shift_filtrado = dft_shift * mascara
            # Deshacer el desplazamiento del cero de frecuencia
            dft_filtrado = np.fft.ifftshift(dft_shift_filtrado)
            # Transformada Inversa de Fourier 2D
            canal_filtrado = np.fft.ifft2(dft_filtrado)
            # Obtener la magnitud del resultado complejo
            canal_filtrado = np.abs(canal_filtrado)
            c_filtrados.append(canal_filtrado)

        # Combinar los canales filtrados en una imagen
        imagen_filtrada = cv2.merge(c_filtrados)
        return imagen_filtrada

    #hace que se realce los bordes en las imagenes. 
    def pasa_altas(self, frec_corte):
        c_filtrados = []
        for canal in cv2.split(self.imagen):
            # Transformada de Fourier 2D
            dft = np.fft.fft2(canal)
            # Desplazamiento del cero de frecuencia al centro del espectro
            dft_shift = np.fft.fftshift(dft)

            # Crear una máscara de paso alto (invertir la máscara de paso bajo)
            filas, columnas = canal.shape
            centro_filas, centro_columnas = filas // 2, columnas // 2
            mascara = np.ones((filas, columnas), np.uint8)
            radio = int(min(filas, columnas) * frec_corte)
            cv2.circle(mascara, (centro_columnas, centro_filas), radio, 0, thickness=-1)

            # Aplicar la máscara al DFT
            dft_shift_filtrado = dft_shift * mascara
            # Deshacer el desplazamiento del cero de frecuencia
            dft_filtrado = np.fft.ifftshift(dft_shift_filtrado)
            # Transformada Inversa de Fourier 2D
            canal_filtrado = np.fft.ifft2(dft_filtrado)
            # Obtener la magnitud del resultado complejo
            canal_filtrado = np.abs(canal_filtrado)
            c_filtrados.append(canal_filtrado)

        # Combinar los canales filtrados en una imagen
        imagen_filtrada = cv2.merge(c_filtrados)
        return imagen_filtrada

    def display_filtered_img(self, frec_corte):
        # Aplicar filtros de paso bajo y paso alto
        imgs_pasa_bajas = [self.pasa_bajas(self.imagen, f) for f in frec_corte]
        imgs_pasa_altas = [self.pasa_altas(self.imagen, f) for f in frec_corte]

        plt.figure(figsize=(18, 12))

        plt.subplot(3, 4, 1)
        plt.title("Imagen Original")
        plt.imshow(cv2.cvtColor(self.imagen, cv2.COLOR_BGR2RGB))
        plt.axis("off")

        for i, (imagen_filtrada, f) in enumerate(zip(imgs_pasa_bajas, frec_corte), start=2):
            plt.subplot(3, 4, i)
            plt.title(f"Filtro Pasa Bajas (corte = {f})")
            plt.imshow(cv2.cvtColor(imagen_filtrada.astype(np.uint8), cv2.COLOR_BGR2RGB))
            plt.axis("off")

        for i, (imagen_filtrada, f) in enumerate(zip(imgs_pasa_altas, frec_corte), start=6):
            plt.subplot(3, 4, i + 4)
            plt.title(f"Filtro Pasa Altas (corte = {f})")
            plt.imshow(cv2.cvtColor(imagen_filtrada.astype(np.uint8), cv2.COLOR_BGR2RGB))
            plt.axis("off")

        #plt.tight_layout()
        #plt.show()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        return img_base64
