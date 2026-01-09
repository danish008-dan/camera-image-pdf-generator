# PURPOSE OF THIS FILE:
# This script takes person's name as input, opens the camera,
# captures 200 images of that person, and stores them inside a folder
# named after that person. These images will later be added into a PDF file.

import cv2  # Importing OpenCV library for camera handling
import os   # Importing OS library to work with folders and paths

# Asking user to input person's name
person_name = input("Enter person's name: ")

# Creating a folder name using person's name
folder_name = person_name

# If this folder does not exist, then create it
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Opening default camera (0 means default laptop/USB camera)
camera = cv2.VideoCapture(0)

# Variable to count number of photos taken
count = 0

# Loop continues until 200 images are captured
while True:
    # Reading frame from camera
    ret, frame = camera.read()

    # If frame not read successfully, break loop
    if not ret:
        break

    # Showing live camera preview window
    cv2.imshow("Camera - Press q to quit", frame)

    # Creating filename for each image
    image_name = folder_name + "/img_" + str(count + 1) + ".jpg"

    # Saving the current frame as image
    cv2.imwrite(image_name, frame)

    # Increasing the image count
    count += 1

    # If 200 images captured, exit loop
    if count == 200:
        break

    # Checking if user presses 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releasing the camera resource
camera.release()

# Closing camera preview window
cv2.destroyAllWindows()

# Printing completion message
print("200 images captured and saved in folder:", folder_name)
