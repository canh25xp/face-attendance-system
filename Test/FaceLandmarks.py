import face_recognition
import cv2


image = face_recognition.load_image_file("meme.jpg")

# Convert the image to RGB format (required by OpenCV)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Input", image_rgb)

face_landmarks_list = face_recognition.face_landmarks(image)


# Draw facial landmarks on the image
for face_landmarks in face_landmarks_list:
    for feature, points in face_landmarks.items():
        for point in points:
            cv2.circle(image_rgb, point, 2, (0, 255, 0), -1)

# Convert back to BGR format for display
# image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# Display the image with facial landmarks
cv2.imshow('Facial Landmarks', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()