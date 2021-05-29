from skimage import io
import numpy as np
from facenet_pytorch import MTCNN


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

    url_to_image(image_url) -> image : numpy.ndarray
        this method take an url image and convert it to numpy.ndarray
    """

    def extract_face_to_list(self, image):
        mtcnn = MTCNN(margin=20, keep_all=True,
                      post_process=False, device='cuda:0')
        faces = mtcnn(image)

        list_of_faces = []
        if faces is None:
            list_of_faces.append("Image Not Found")
            return list_of_faces

        for face in faces:
            face_array = face.permute(1, 2, 0).int().numpy()
            list_of_faces.append(face_array)

        return list_of_faces

    def url_to_image(self, image_url):
        image = io.imread(image_url)
        return image
