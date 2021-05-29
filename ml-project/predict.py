# -*- coding: utf-8 -*-

import cv2 
import numpy as np 
import mtcnn 
from model_architecture import *
from sklearn.preprocessing import Normalizer
from scipy.spatial.distance import cosine
from tensorflow.keras.models import load_model
import pickle
import sys
import os


recognition_t=0.5
required_size = (160,160)

def normalize(img):
    mean, std = img.mean(), img.std()
    return (img - mean) / std

def get_encode(face_encoder, face, size):
    face = normalize(face)
    face = cv2.resize(face, size)
    encode = face_encoder.predict(np.expand_dims(face, axis=0))[0]
    return encode

def load_pickle(path):
    with open(path, 'rb') as f:
        encoding_dict = pickle.load(f)
    return encoding_dict

def detect(img ,detector,encoder,encoding_dict):
    """Detect And Return Result
    Parameters
    ----------
    img : str
        Image path you want to predict.
    detector : MTCNN object
        MTCNN object constructor
        ex : detector = mtcnn.MTCNN()
    encoder : model_object
        Its our pretrained weight
        ex : encoder = InceptionResNetV2().load_weights(weight_path)
    encoding_dict : pickle_load_object
        ex : encoding_dict = load_pickle(encodings_path)
    """

    l2_normalizer = Normalizer('l2')
    img = cv2.imread(img)
    if img is None:
      print("Genki desuka?")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Detect Face In Image
    results = detector.detect_faces(img_rgb)
    
    encode = get_encode(encoder, img_rgb, required_size)
    encode = l2_normalizer.transform(encode.reshape(1, -1))[0]

    name = "unknown"

    distance = float("inf")
    for pred_name, db_encode in encoding_dict.items():
        dist = cosine(db_encode, encode)
        # Jika semakin dekat or "dist is low" the accuracy is high
        if dist < recognition_t and dist < distance:
                name = pred_name
                distance = dist
                detection_percentage = [name, distance]


    if name == "unknown":
        print("Doesnt recognize")
        detection_percentage = [name, 0.0]
    else:
        print("This is {} with Distance {}".format(name, distance))
    
    return detection_percentage

def predict(folder_path, path_encoding, model_path):
    prediction = []
    face_detector = mtcnn.MTCNN()
    face_encoder = InceptionResNetV2() 
    weight_path = model_path
    face_encoder.load_weights(weight_path)
    encoding_path = path_encoding
    encoding_dict = load_pickle(encoding_path)
    for filename in os.listdir(folder_path):
      if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
          prediction_percentage = detect(os.path.join(folder_path,filename), face_detector, face_encoder, encoding_dict)
          dictionary = {'name':prediction_percentage[0], 'percentage': prediction_percentage[1], 'url':os.path.join(folder_path,filename)}
          prediction.append(dictionary)
      else:
        pass

    return prediction

if __name__ == "__main__":
    
    if len(sys.argv) < 4:
        print("Usage: python predict.py 'Folder_path' 'Encoding_path.pkl' 'Model_path.h5'")
        sys.exit()

    if os.path.isdir(sys.argv[1]) == False:
        print("Couldn't find folder!")
    else:
        if os.path.isfile(sys.argv[2]) == False:
            print("Couldn't find encodings.pkl file!")
        else:
            if os.path.isfile(sys.argv[3]) == False:
                print("Couldn't find model.h5 file!")
            else:
                predict(sys.argv[1], sys.argv[2], sys.argv[3])
        

        