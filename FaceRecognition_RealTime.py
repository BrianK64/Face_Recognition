import cv2
import random

cascade_path = r'C:\Users\Brian\Desktop\Coding\Python\AI\haarcascade_frontalface_default.xml'

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(cascade_path)

# Capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames
while True:
    
    # Read the current frame
    successful_grame_read, frame = webcam.read()

    # Convert to grayscale
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # Detext faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (random.randrange(256), random.randrange(256), random.randrange(256)), 2)
    
    cv2.imshow('Face Recognition', frame)
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

print("Code Completed")