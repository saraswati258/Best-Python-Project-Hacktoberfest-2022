import cv2
from random import randrange

# Load some pre-trained data on Face frontal from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose an image to check the face is detected
img = cv2.imread("Steve and Bill.jpg")


# Must convert to gray scale
gray_scaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(gray_scaled_img)

# Draw rectangles around the face
# (randrange(256), randrange(256), randrange(256)) -> This is responsible for the color
# 2 -> This is the thickness of the border 
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

# Display image with face spotted
cv2.imshow("Joel's Face Detector!!", img)
cv2.waitKey()

print("Code Finished")
