import cv2
import numpy as np
import mtcnn
from model_architecture import *
from sklearn.preprocessing import Normalizer
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model
import pickle


class Predict:
    """
    Predict class is class that responsible for predicting identity based on face

    ...

    Methods
    -------
    normalize(image: numpy ndarray) -> int: (face - mean) / std
        returning value for normalization for image input

    get_encode(API face encoder, image: numpy ndarray, image: size) -> MTCNN object
        this method take an numpy ndarray ans it's size then pass it to MTCNN to get encode for MTCNN object, later MTCNN object used to encode face input

    load_pickle(str_path: .pkl file for encodings) -> dictionary: encoding_dictionary
        this method read .pkl file to generate encoding_dictionary, later encoding_dictionary used to extract label and it's encoder value for predicting

    raw_predict(image: numpy ndarray, MTCNN API, MTCNN object, encoding_dictionary) -> list: [label, confidence value]
        this method take face input (an numpy ndarray) then pass it to MTCNN API with it's MTCNN object to get face encoder value. Then the face encoder value will be compare with 
        bunch of face encoder values in encoding_dictionary. The result of comparing is to get the nearest value of a label that best decribe the face input. The return of this function
        if a list that contain prediction label with it's prediction score

    predict_face(image: numpy ndarray, str_path: .pkl file for encodings, str_path: .h5 file for model) -> list: [dictionary: {'name': label, 'percentage': prediction score}]
        this method take image: numpy ndarray, str_path: .pkl file for encodings, str_path: .h5 file for model then pass image: numpy ndarray, MTCNN API, MTCNN object, encoding_dictionary
        to raw_predict. The return of this function is to get list that conating dictionary of label prediction and it's prediction score

    """

    def __init__(self, pkl_path, model_path):

        self.pkl_path = pkl_path
        self.model_path = model_path

        self.face_encoder = InceptionResNetV2()
        self.face_encoder.load_weights(self.model_path)
        self.encoding_dict = self.load_pickle(self.pkl_path)

    # Global variable
    recognition_t = 0.5
    required_size = (160,160)

    # Normalization
    def normalize(self, face):
        mean, std = face.mean(), face.std()
        return (face - mean) / std

    # Encode face after normalization
    def get_encode(self, face_encoder, face, size):
        face = self.normalize(face)
        face = cv2.resize(face, size)
        encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
        return encode

    # Load pickle file
    def load_pickle(self, path):
        with open(path, 'rb') as f:
            encoding_dict = pickle.load(f)
        return encoding_dict

    # Detect face
    def raw_predict(self, face, encoder, encoding_dict):
        l2_normalizer = Normalizer('l2')
        # face = cv2.imread(face)
        # if face is None:
        #     print("Image not Found!")
        # face_rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        # Detect Face In Image
        # results = detector.detect_faces(face_rgb)

        encode = self.get_encode(encoder, face, self.required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]

        name = "unknown"

        distance = float("inf")
        for pred_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            # Jika semakin dekat or "dist is low" the accuracy is high
            if dist < self.recognition_t and dist < distance:
                name = pred_name
                distance = dist
                detection_percentage = [name, distance]

        if name == "unknown":
            print("Doesnt recognize")
            detection_percentage = [name, 0.0]
        else:
            print("This is {} with Distance {}".format(name, distance))

        return detection_percentage

    # PredictFace
    def predict_face(self, face):
        prediction = []

        prediction_percentage = self.raw_predict(
            face, self.face_encoder, self.encoding_dict)
        dictionary = {
            'name':prediction_percentage[0], 'percentage': prediction_percentage[1]}
        prediction.append(dictionary)
        return prediction
