import numpy as np

def numpyarray_to_blob(numpyArray):
    blob_file = numpyArray.tobytes()
    return blob_file
