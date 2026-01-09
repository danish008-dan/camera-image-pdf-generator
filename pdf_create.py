# PURPOSE OF THIS FILE:
# This script reads all the images of a person from their folder
# and stores these images inside a single PDF file.
# Each image will be placed on a separate page of the PDF.
# The PDF will be saved inside the same person folder.

import os  # For working with folders and files
from reportlab.lib.pagesizes import A4  # Standard A4 page size for PDF
from reportlab.pdfgen import canvas  # Used to create PDF and draw images

# Asking user to enter the same person's name used in Phase 1
person_name = input("Enter person's name (same as Phase 1): ")

# Folder where person's images are stored
folder_name = person_name

# Creating full PDF file path like: personname/personname_images.pdf
pdf_path = os.path.join(folder_name, person_name + "_images.pdf")

# Creating a PDF canvas object to draw content
c = canvas.Canvas(pdf_path, pagesize=A4)

# Getting list of all image files inside the folder
images = sorted(os.listdir(folder_name))

# Loop through each file inside folder
for img in images:
    # Full path of current image
    img_path = os.path.join(folder_name, img)

    # Check if file is really an image by extension
    if img_path.lower().endswith((".jpg", ".jpeg", ".png")):

        # Draw the image on PDF page (0,0 bottom-left corner)
        # width & height roughly A4 page size
        c.drawImage(img_path, 0, 0, width=595, height=842)

        # After each image, add new PDF page
        c.showPage()

# Save the final PDF
c.save()

# Print success message
print("PDF created successfully at:", pdf_path)
