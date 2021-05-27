# Embedding flow
![Embedding Process](https://github.com/mozarik/bangkit-capstone-CAP0166/blob/develop/assets/model-training-flow.jpg)

# Predict flow
![Predict Process](https://github.com/mozarik/bangkit-capstone-CAP0166/blob/develop/assets/predict-workflow.jpg)

# How To Run 
## train.py 

To run train.py you need to prepare a directory with this structure. You may need like 15-20 Image of that person face

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
