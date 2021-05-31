from facenet_pytorch import MTCNN

import cv2
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import sys
import os
import traceback
import argparse


def extract_face(image_path, save_path):
    """ Extract individual faces to a save_path

    Parameters
    ----------
    image_path : str
        image path of many faces that you want to extract
    print_cols : str
        save_path is where you want to save individual face image

        example: 
            save_path="face.jpg". it will create an individual faces with filename
            face{i}.jpg where i is incremental from 1 to number of faces

    Returns
    -------
    None
    """

    mtcnn = MTCNN(margin=20, keep_all=True,
                  post_process=False)
    image = image_path
    image = mpimg.imread(image)
    image = Image.fromarray(image)
    mtcnn(image, save_path=save_path)


def command_line_parser():
    """ Hmmm well return all the parser argument

    Returns
    -------
    Return args parser
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=str,
                        help="Image you want to extract individual faces")
    parser.add_argument("save_path", type=str,
                        help="Save image path of individual faces ex:Extracted/face.jpg")
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = command_line_parser()
    extract_face(args.image_path, args.save_path)
