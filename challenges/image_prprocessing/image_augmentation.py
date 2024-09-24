import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# Paths setup - change these if needed
input_folder = 'input_images'  # Where we get the original images from
output_folder = 'augmented_images'  # Where we’re gonna save these fancy new augmented images

# Create output directory if it ain't there yet
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define the image size for resizing - again, make this whatever fits your setup
target_size = (128, 128)

# Function to add some noise, y'know, spice things up
def add_gaussian_noise(image):
    mean = 0  # keeping it chill at zero mean
    std = 25  # control the madness - higher value, more noise
    noise = np.random.normal(mean, std, image.shape)
    noisy_image = image + noise
    return np.clip(noisy_image, 0, 255).astype(np.uint8)

# Alright, let's loop through these bad boys
for image_name in os.listdir(input_folder):
    if image_name.endswith('.png') or image_name.endswith('.jpg'):
        # Read and preprocess the image
        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path)

        # Convert to grayscale, just like before
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize image to fit our target size
        resized_image = cv2.resize(grayscale_image, target_size)

        # 1. Save the original, 'cause why not?
        cv2.imwrite(os.path.join(output_folder, f"original_{image_name}"), resized_image)

        # 2. Rotate it - let's spin this image 90 degrees
        rotated_image = cv2.rotate(resized_image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(output_folder, f"rotated_{image_name}"), rotated_image)

        # 3. Flip it horizontally - like a mirror but not for selfies
        flipped_horiz = cv2.flip(resized_image, 1)
        cv2.imwrite(os.path.join(output_folder, f"flipped_horiz_{image_name}"), flipped_horiz)

        # 4. Flip it vertically - just for fun
        flipped_vert = cv2.flip(resized_image, 0)
        cv2.imwrite(os.path.join(output_folder, f"flipped_vert_{image_name}"), flipped_vert)

        # 5. Adjust brightness - let's make it pop (increase brightness)
        bright_image = cv2.convertScaleAbs(resized_image, alpha=1.5, beta=20)
        cv2.imwrite(os.path.join(output_folder, f"bright_{image_name}"), bright_image)

        # 6. Add Gaussian noise - make it look like an old TV screen
        noisy_image = add_gaussian_noise(resized_image)
        cv2.imwrite(os.path.join(output_folder, f"noisy_{image_name}"), noisy_image)

        print(f"Augmented and saved versions of: {image_name}")

print("Image augmentation done, buddy! 🎉")
