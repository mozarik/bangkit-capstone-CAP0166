import sys
import os
import traceback
from PIL import Image
from facenet_pytorch import MTCNN
import matplotlib.image as mpimg
import numpy as np


def detect_faces(image_path):
    mtcnn = MTCNN(margin=20, keep_all=True,
                  post_process=False, device='cuda:0')
    image = image_path
    image = mpimg.imread(image)
    image = Image.fromarray(image)
    faces = mtcnn(image)
    count = 0
    for face in faces:
        face = face.permute(1, 2, 0).int().numpy()
        # cv2.imwrite(os.path.join(
        #     path_folder, "face" + str(count) + ".jpg"),face)
        face = Image.fromarray((face).astype(np.uint8))
        face.save(os.path.join(path_folder, "face" + str(count) + ".jpg"))
        count = count + 1


if __name__ == "__main__":
    fcount = 0
    while os.path.exists("ExtractedFaceFolder" + str(fcount)) == True:
        fcount = fcount + 1
        if os.path.exists("ExtractedFaceFolder" + str(fcount)) == False:
            break
        else:
            continue
    os.mkdir("ExtractedFaceFolder" + str(fcount))
    path_folder = "ExtractedFaceFolder" + str(fcount)

    if len(sys.argv) < 2:
        print("Usage: python detect_extract_save.py 'image path'")
        sys.exit()

    if os.path.isdir(sys.argv[1]):
        for image in os.listdir(sys.argv[1]):
            try:
                print("Processing.....",os.path.abspath(
                    os.path.join(sys.argv[1],image)))
                detect_faces(os.path.abspath(
                    os.path.join(sys.argv[1],image)),False)
            except Exception:
                print("Could not process ",os.path.abspath(
                    os.path.join(sys.argv[1],image)))
    else:
        detect_faces(sys.argv[1])
