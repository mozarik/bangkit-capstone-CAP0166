import numpy as np
from cv2 import cv2

def numpyarray_to_blob(numpyArray: np):
    success, encoded_image = cv2.imencode('.jpg', numpyArray)
    blob_file = encoded_image.tobytes()
    return blob_file
