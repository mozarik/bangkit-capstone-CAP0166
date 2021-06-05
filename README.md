![Logo](https://raw.githubusercontent.com/mozarik/bangkit-capstone-CAP0166/main/.github/images/the-watcher.png)
# Bangkit 2021 Capstone Team : CAP0166

Hi. this is our repository for our project. Our team consist of 2 people from each Bangkit Path which is consist of Machine Learning, Android, and Cloud Computing.


All of the project management will take place on Github using the project board. 

## Our Team Member 

|          Nama         | Bangkit-ID |       Path       |
|:---------------------:|:----------:|:----------------:|
|  Muhammad Zein I. F.  |  M2582405  | Machine Learning |
|   Yusril Hasanuddin   |  M2582412  | Machine Learning |
|    Salsha Farahdiba   |  C2472321  |  Cloud Computing |
|         Fachry        |  C2582415  |  Cloud Computing |
| Salsabila Khairunnisa |  A0050361  |      Android     |
|    Antoni Kurniawan   |  A0050366  |      Android     |

## What Are We Doing In This Project
We make automatic students presence by using both Face detection and Face recognition to identify a person based on their faces




## Tech Stack And Workflow

### Tech Stack
- Python
- 

## Local Deployment Machine Learning Jupyter Notebook
Make sure you intalled this dependency first on your local machine. You can use `virtual-env` or conda virtual env for making things easier
```text
scikit-image==0.18.1
facenet-pytorch==2.5.2
matplotlib==3.4.2
validators==0.18.2
opencv-python==4.5.2.52
scikit-learn==0.24.2
mtcnn==0.1.0
tensorflow==2.4.1
```

For using our machine learning example first you need to clone our project or fork our project by using this line 

`git clone https://github.com/mozarik/bangkit-capstone-CAP0166.git bangkit-project`

after that there is a folder called `bangkit-project`. The next step is **Generating Your Dataset**

There is 2 way to generate your training data.

- By deepfaking your photo by using `generate_data_deepfake.ipynb` or you can go to this notebook [Generate Deepfake Data](https://colab.research.google.com/drive/1d0Y9WYcXktoE4zcR9TwByjWIJg1L31LX?usp=sharing) 
- Or you can use your selfie photo make sur to use 1:1 resolution for better accuracy. 

After you done making the dataset go first you need to make a directory structure like this. The name filename does not matter as long you put the Name of the person as the directory.

For training the data you will need a image of a person face but in that image there's only one picture  
```
├───image
│   ├───Brad_Pitt
│   │       bradd_1.jpg
│   │       bradd_2.jpg
│   │       bradd_3.jpg
│   │       bradd_4.jpg
│   │       bradd_5.jpg
│   │
│   ├───Yusril
│   │       yusril_1.jpg
│   │       yusril_2.jpg
│   │       yusril_3.jpg
│   │       yusril_4.jpg
│   │       yusril_5.jpg
│   │       yusril_6.jpg
│   │       yusril_7.jpg
│   │       yusril_8.jpg
``` 
cd to `/ml-project`And then run.  `python .\train.py <your-image_dataset-directory> model\facenet_keras_weights.h5`

after this you will see a  `encodings.pkl`

You can use `encodings.pkl` as your embedding file. 

For example see `playground_example_zein.ipynb` to run the inference. 



## Project Update

**TBD** 
