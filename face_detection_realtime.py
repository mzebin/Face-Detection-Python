# Importing required modules.
import sys
import cv2

# Getting the path to the cascade.
cascade_path = sys.argv[1]

# Creating the haar cascade.
face_cascade = cv2.CascadeClassifier(cascade_path)

# Setting the video source to webcam.
video_capture = cv2.VideoCapture(0)

while True:
	# Capture the frame.
	ret, frame = video_capture.read()
	grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detecting faces in the image.
	faces = face_cascade.detectMultiScale(
		grey,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
	)

	# Drawing rectangle around the faces.
	for x, y, w, h in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# Display the result.
	cv2.imshow("Video", frame)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# Release the capture and destroy the windows.
video_capture.release()
cv2.destroyAllWindows()
