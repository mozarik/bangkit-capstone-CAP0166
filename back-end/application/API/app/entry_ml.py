import numpy as np


def numpyarray_to_blob(numpyArray: np):
    blob_file = numpyArray.tobytes
    return blob_file
