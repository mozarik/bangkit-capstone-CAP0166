from model_architecture import *
import os
import cv2
import mtcnn
import pickle
import numpy as np
from sklearn.preprocessing import Normalizer
from tensorflow.keras.models import load_model
import tensorflow as tf
import argparse


def normalize(img):
    mean, std = img.mean(), img.std()
    return (img - mean) / std


def command_line_parser():
    """ Hmmm well return all the parser argument ;)

    Returns
    -------
    Return args parser
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("face_data", type=str,
                        help="Face data ex: 'image/' is a folder where every enrolled student format: image/studentName/[list_of_photo]")
    parser.add_argument("weight_path", type=str,
                        help="Pretrained keras weight path")
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = command_line_parser()
    face_data = args.face_data
    path = args.weight_path
    face_encoder = InceptionResNetV2()
    face_encoder.load_weights(path)

    required_shape = (160,160)
    face_detector = mtcnn.MTCNN()
    encodes = []
    encoding_dict = dict()
    l2_normalizer = Normalizer('l2')

    for face_names in os.listdir(face_data):
        person_dir = os.path.join(face_data,face_names)

        for image_name in os.listdir(person_dir):
            image_path = os.path.join(person_dir,image_name)

            img_BGR = cv2.imread(image_path)
            img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

            # GETTING THE FACE ONLY
            x = face_detector.detect_faces(img_RGB)
            x1, y1, width, height = x[0]['box']
            x1, y1 = abs(x1) , abs(y1)
            x2, y2 = x1 + width , y1 + height
            face = img_RGB[y1:y2 , x1:x2]

            # NORMALIZE THE DATA AND DO PREDICTION AND ENCODING
            face = normalize(face)
            face = cv2.resize(face, required_shape)
            face_d = np.expand_dims(face, axis=0)
            encode = face_encoder.predict(face_d)[0]
            encodes.append(encode)

        if encodes:
            encode = np.sum(encodes, axis=0)
            encode = l2_normalizer.transform(
                np.expand_dims(encode, axis=0))[0]
            encoding_dict[face_names] = encode

    path = 'encodings.pkl'
    with open(path, 'wb') as file:
        pickle.dump(encoding_dict, file)
