from fft import ImageFilter
import os

image_path = os.getcwd()
cutoff_frequencies = [0.2, 0.1, 0.9]

img_names = ['img1.jpeg', 'img2.png', 'img3.jpg', 'img4.jpg']
final_path = f"{image_path}/backend/img/{img_names[0]}".replace("\\", "/")
# llamar a funcion de filtrado
print(f">>> {final_path}")
print(f">>> {image_path}")
image_filter = ImageFilter(final_path)
image_filter.display_filtered_img(cutoff_frequencies)

