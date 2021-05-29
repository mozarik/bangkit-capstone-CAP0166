from extract import Extract
import numpy as np
from skimage import io

IMAGE_URL = "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg"


def test_url_to_image():
    extract = Extract()
    image = extract.url_to_image(IMAGE_URL)
    assert isinstance(image, np.ndarray)


def test_extract_to_list_return_np_ndarray():
    image = np.zeros((300,300,3))
    extract = Extract()
    list_of_faces = extract.extract_face_to_list(image)

    if type(list_of_faces[0]) is str:
        assert isinstance(list_of_faces[0], str)
    else:
        assert isinstance(list_of_faces[0], np.ndarray)
