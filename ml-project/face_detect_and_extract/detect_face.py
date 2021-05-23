import cv2
import sys
import os
import traceback
      
CASCADE="C:/Users/ACER/Downloads/ExtractFace/Face_Detect/Face_cascade.xml"
FACE_CASCADE=cv2.CascadeClassifier(CASCADE)

def detect_faces(image_path,display=True):

	image=cv2.imread(image_path)
	image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

	faces = FACE_CASCADE.detectMultiScale(image_grey,scaleFactor=1.16,minNeighbors=5,minSize=(25,25),flags=0)

	newcount = 0

	for x,y,w,h in faces:
		sub_img=image[y-10:y+h+10,x-10:x+w+10]
		os.chdir(path_folder)
		cv2.imwrite("image"+str(newcount)+".jpg",sub_img)
		os.chdir("../")
		cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
		newcount = newcount + 1
	
	if display:
		cv2.imshow("Faces Found",image)
		# if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
		# 	cv2.destroyAllWindows()
	cv2.destroyAllWindows()

if __name__ == "__main__":
    
	count = 0
	while os.path.exists("C:/Users/ACER/Downloads/ExtractFace/Face_Detect/ExtractedFaceFolder" + str(count)) == True:
		count = count + 1
		if os.path.exists("C:/Users/ACER/Downloads/ExtractFace/Face_Detect/ExtractedFaceFolder" + str(count)) == False:
			break
		else:
			continue
	os.mkdir("C:/Users/ACER/Downloads/ExtractFace/Face_Detect/ExtractedFaceFolder" + str(count))
	path_folder = "C:/Users/ACER/Downloads/ExtractFace/Face_Detect/ExtractedFaceFolder" + str(count)

	if len(sys.argv) < 2:
		print("Usage: python Detect_face.py 'image path'")
		sys.exit()

	if os.path.isdir(sys.argv[1]):
		for image in os.listdir(sys.argv[1]):
			try:
				print ("Processing.....",os.path.abspath(os.path.join(sys.argv[1],image)))
				detect_faces(os.path.abspath(os.path.join(sys.argv[1],image)),False)
			except Exception:
				print ("Could not process ",os.path.abspath(os.path.join(sys.argv[1],image)))
	else:
		detect_faces(sys.argv[1])