import face_recognition
import cv2


image = face_recognition.load_image_file("meme.jpg")
face_locations = face_recognition.face_locations(image)

# Convert the image to RGB format (required by OpenCV)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("Input", image_rgb)

# Print the coordinates of each detected face
for face_location in face_locations:
    top, right, bottom, left = face_location
    print(f"Face found at coordinates: Top: {top}, Right: {right}, Bottom: {bottom}, Left: {left}")
    cv2.rectangle(image_rgb, (left, top), (right, bottom), (0, 255, 0), 2)

# Convert back to BGR format for display
# image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

# Display the image with bounding boxes
cv2.imshow('Detected Faces', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
