from extract import Extract
from predict import Predict
from matplotlib import pyplot as plt
import cv2
import numpy as np
from predict import Predict
from extract import Extract
import mtcnn
from facenet_pytorch import MTCNN


class BigGiant:
    def __init__(self, pkl_path, model_path):
        self.pkl_path = pkl_path
        self.model_path = model_path
        self.predict = Predict(self.pkl_path, self.model_path)
        self.extract = Extract()
        self.mtcnn = MTCNN()

    def extract_face_to_list(self, image):
        list_of_faces = self.extract.extract_face_to_list(image)
        return list_of_faces

    def predict_face(self, face):
        data = self.predict.predict_face(face)
        return data

    def read_image(self, image_path):
        image = self.extract.read_image(image_path)
        return image

    def aggregate_face_data(self, data, image_url):
        pass


def insert_data_to_db(data):
    pass


def upload_face_to_bucket(face):
    pass


def main(image):
    pkl_path = "X:\\bangkit-project\\ml-project\\encodings-demo.pkl"
    model_path = "X:\bangkit-project\ml-project\model\facenet_keras_weights.h5"
    BG = BigGiant(pkl_path, model_path)

    image = extract.read_image(image_path)
