# Embedding flow
![Embedding Process](https://github.com/mozarik/bangkit-capstone-CAP0166/blob/develop/assets/model-training-flow.jpg)

# Predict flow
![Predict Process](https://github.com/mozarik/bangkit-capstone-CAP0166/blob/develop/assets/predict-workflow.jpg)

# How To Run 
## train.py 

To run `train.py` you need to prepare a directory with this structure. You may need like 15-20 Image of that person face

```
├───Brad_Pitt
│       bradd_1.jpg
│       ---
│       bradd_n.jpg
├───Yusril
│       yusril_1.jpg
|       ---
│       yusril_n.jpg
└───Zein
        zein_1.jpg
        ---
        zein_n.jpg
```

And then run.
`python ./train.py image/ model/facenet_keras_weights.h5`

after this you will see a `encodings.pkl`

## save_extract_face.py

`save_extract_face.py` is used for extracting faces in a picture and save it to a folder 

Run : `python .\save_extract_face.py 6_faces.jpg Extracted2/face.jpg` 

this will output a directory with this structure. each file is a single face in given picture.
```
EXTRACTED2
|    face.jpg
|    face_2.jpg
|    face_3.jpg
|    face_4.jpg
|    face_5.jpg
|    face_6.jpg
```
