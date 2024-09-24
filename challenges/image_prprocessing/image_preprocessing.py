 
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Define paths (Change these paths as per your folder structure)
input_folder = 'input_images'   # Folder containing your original images
output_folder = 'processed_images'  # Folder where processed images will be saved

# Create output directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define image size for resizing
target_size = (128, 128)  # You can adjust this size as needed

# Load and process images
for image_name in os.listdir(input_folder):
    if image_name.endswith('.png') or image_name.endswith('.jpg'):  # Process only image files
        # Read the image
        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path)

        # Convert to grayscale
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize image
        resized_image = cv2.resize(grayscale_image, target_size)

        # Save processed image
        output_path = os.path.join(output_folder, f"processed_{image_name}")
        cv2.imwrite(output_path, resized_image)

        print(f"Processed and saved: {output_path}")

print("Image preprocessing completed!")
