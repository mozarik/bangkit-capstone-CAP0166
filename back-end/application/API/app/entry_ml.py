import numpy as np
from cv2 import cv2


def numpyarray_to_blob(numpyArray: np):
    numpyArray = cv2.cvtColor(numpyArray, cv2.COLOR_BGR2RGB)
    success, encoded_image = cv2.imencode('.jpg', numpyArray)
    blob_file = encoded_image.tobytes()
    return blob_file
