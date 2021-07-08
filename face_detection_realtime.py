# Importing required modules.
import sys
import cv2

# Getting the path to the cascade.
cascade_path = sys.argv[1]

# Creating the haar cascade.
face_cascade = cv2.CascadeClassifier(cascade_path)

# Setting the video source to webcam.
video_capture = cv2.VideoCapture(0)
