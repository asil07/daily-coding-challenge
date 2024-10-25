import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Set up directories
input_dir = 'input_images/'  # Folder with original histopathological images
output_dir = 'augmented_images/'  # Folder to save augmented images

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to load image
def load_image(file_path):
    img = cv2.imread(file_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

# Function to save augmented image
def save_augmented_image(img, filename):
    output_path = os.path.join(output_dir, filename)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, img)

# Initialize ImageDataGenerator for augmentation
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Perform data augmentation on a sample of images
for img_name in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_name)
    img = load_image(img_path)
    img = np.expand_dims(img, axis=0)  # Expand dimensions to fit the generator

    # Generate 5 augmented images per input image
    i = 0
    for batch in datagen.flow(img, batch_size=1):
        augmented_img = batch[0].astype('uint8')
        save_augmented_image(augmented_img, f"aug_{i}_{img_name}")
        
        i += 1
        if i >= 5:  # Limit the number of augmented images per input
            break

    # Display one augmented image for reference
    if i == 5:
        plt.imshow(augmented_img)
        plt.title(f"Augmented version of {img_name}")
        plt.show()