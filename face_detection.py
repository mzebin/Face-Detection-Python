# Importing Required Modules.
import sys
import cv2

# Getting the path to the image and cascade.
image_path = sys.argv[1]
cascade_path = sys.argv[2]

# Creating the haar cascade.
face_cascade = cv2.CascadeClassifier(cascade_path)

# Reading the image.
image = cv2.imread(image_path)
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecting Faces.
faces = face_cascade.detectMultiScale(
	image_grey,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
)

# Drawing rectangle around the faces.
for x, y, w, h in faces:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image.
cv2.imshow("Faces Found", image)
cv2.waitKey(0)
