import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_low_pass_filter(image, cutoff_frequency):
    filtered_channels = []
    for channel in cv2.split(image):
        dft = np.fft.fft2(channel)
        dft_shift = np.fft.fftshift(dft)

        # Create a low-pass mask
        rows, cols = channel.shape
        crow, ccol = rows // 2, cols // 2
        mask = np.zeros((rows, cols), np.uint8)
        radius = int(min(rows, cols) * cutoff_frequency)
        cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)

        # Apply mask to DFT
        filtered_dft_shift = dft_shift * mask
        filtered_dft = np.fft.ifftshift(filtered_dft_shift)
        filtered_channel = np.fft.ifft2(filtered_dft)
        filtered_channel = np.abs(filtered_channel)
        filtered_channels.append(filtered_channel)

    filtered_image = cv2.merge(filtered_channels)
    return filtered_image

def apply_high_pass_filter(image, cutoff_frequency):
    filtered_channels = []
    for channel in cv2.split(image):
        dft = np.fft.fft2(channel)
        dft_shift = np.fft.fftshift(dft)

        # Create a high-pass mask (invert the low-pass mask)
        rows, cols = channel.shape
        crow, ccol = rows // 2, cols // 2
        mask = np.ones((rows, cols), np.uint8)
        radius = int(min(rows, cols) * cutoff_frequency)
        cv2.circle(mask, (ccol, crow), radius, 0, thickness=-1)

        # Apply mask to DFT
        filtered_dft_shift = dft_shift * mask
        filtered_dft = np.fft.ifftshift(filtered_dft_shift)
        filtered_channel = np.fft.ifft2(filtered_dft)
        filtered_channel = np.abs(filtered_channel)
        filtered_channels.append(filtered_channel)

    filtered_image = cv2.merge(filtered_channels)
    return filtered_image

# Load the original color image
image_path = r'C:\Users\jivan\OneDrive - Universidad Galileo\Mate VI\Proyecto\img2.png'
image = cv2.imread(image_path)

# Define cutoff frequencies
cutoff_frequencies = [0.2, 0.1, 0.9]
low_pass_images = [apply_low_pass_filter(image, f) for f in cutoff_frequencies]
high_pass_images = [apply_high_pass_filter(image, f) for f in cutoff_frequencies]

# Display original, low-pass, and high-pass filtered images
plt.figure(figsize=(18, 12))

# Original image
plt.subplot(3, 4, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

# Low-pass filtered images
for i, (filtered_image, f) in enumerate(zip(low_pass_images, cutoff_frequencies), start=2):
    plt.subplot(3, 4, i)
    plt.title(f"Low-Pass Filter (cutoff = {f})")
    plt.imshow(cv2.cvtColor(filtered_image.astype(np.uint8), cv2.COLOR_BGR2RGB))
    plt.axis("off")

# High-pass filtered images
for i, (filtered_image, f) in enumerate(zip(high_pass_images, cutoff_frequencies), start=6):
    plt.subplot(3, 4, i + 4)
    plt.title(f"High-Pass Filter (cutoff = {f})")
    plt.imshow(cv2.cvtColor(filtered_image.astype(np.uint8), cv2.COLOR_BGR2RGB))
    plt.axis("off")

plt.tight_layout()
plt.show()
