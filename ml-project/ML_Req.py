# Phase 1 

# Step 1 

# There's a cemera.
# Camera ini merecognize wajah attendance dalam sebuah canvas 
# Kita bakal memprediksi bahwa orang ini ada dalam canvas sebanyak 100 Iterasi. 
# if 100 iterasi . attendace = True ? attendance = False 

# Problem
# Prediksi 1 orang dulu

# Let say theres a Database with 40 People. 
# every person have 10 pictures with their label based on their NIM.
# We get some state of the art network that already trained to know faces and recognize faces based on their Label. 
# Truncated at least the bottom part of the network 
# And retrain the new 


# 
# Base Model (input=attendance_img.inputs, output=last_layer.outputs)
# Model Kita (Input=base_model.outpus, Output= NIM.outputs)
# We train it based on the attendance_img.
# Saved model.
# Convert it to TFlite.
# Deploy. 
# Test.

our_model = Sequence()
add.Flatten()
add.Dense()
add.Dense(1)


# Phase 2 
# We detect the face using some ML model let say with retinaface => wajah_of_attendance
# Input to Basemodel -> ModelKita -> NIM 

# Phase 3 
# Our ML-TEAM PROBLEM

# Learn about Face Recognition with Video, dan Live-Video (REAL-TIME) -> IMG_FACE_RAW (300,300,3) -> (144,144,3) 5 IMAGE
# maybe we gonna make some helper and util function to help our work.
# Learn about Face Identification -> Yang mana.



True Or Not Distract.


# Yuslir : nge label image person look at the webcam, and doesn't look at their webcam. 
# Video
# Predict(video)
# 1 -> Look at the webcam
# 2 -> Doesnt look at their webcam

