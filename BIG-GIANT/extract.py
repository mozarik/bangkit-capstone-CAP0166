from skimage import io
import numpy as np
from facenet_pytorch import MTCNN
import validators
import matplotlib.image as mpimg
from cv2 import cv2
import urllib.request


def is_image_from_url(url: str):
    valid = validators.url(url)
    if valid == True:
        return True
    else:
        return False


class Extract:
    """
    Extract class is class that responsible for extracting face

    ...

    Attributes
    ----------
    image : numpy.ndarray
        A image with numpy.ndarray type
        You can use matplotlib.image.imread(image_file)
        or use cv2.imread. but remember to convert it back to BGR -> RGB
    Methods
    -------
    extract_face_to_list(image: numpy ndarray) -> list
        returning a list of individual detected image in a list, type(list[0]) == numpy.ndarray

    image_from_url(image_url: str) -> image : numpy.ndarray
        this method take an url image and convert it to numpy.ndarray

    read_image(image_path: str) -> image : numpy.ndarray
        this method read an image from a path or a url and return it as numpy.ndarray
    """

    def extract_face_to_list(self, image):
        mtcnn = MTCNN(margin=20, keep_all=True,
                      post_process=False)
        faces = mtcnn(image)

        list_of_faces = []
        if faces is None:
            list_of_faces.append("Image Not Found")
            return list_of_faces

        for face in faces:
            face_array = face.permute(1, 2, 0).int().numpy()
            face_array = np.array(face_array, dtype='uint8')
            list_of_faces.append(face_array)

        return list_of_faces

    def image_from_url(self, image_url):
        resp = urllib.request.urlopen(image_url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    def image_from_path(self, image_path):
        image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        return image

    def read_image(self, image: str):
        from_url = is_image_from_url(image)

        if from_url is True:
            image_numpy = self.image_from_url(image)
        else:
            image_numpy = self.image_from_path(image)

        return image_numpy
