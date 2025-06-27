import numpy as np
import cv2

def preprocess(image):
    image = image.convert("L")  # grayscale
    image = image.resize((28, 28))
    image = np.array(image)
    image = 255 - image  # invert
    image = image / 255.0
    image = image.reshape(1, 28, 28, 1)
    return image
