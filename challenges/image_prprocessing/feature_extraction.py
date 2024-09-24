import cv2
import os
import numpy as np

# Paths setup - point to the directory with  processed images
input_folder = 'processed_images'  # Folder with preprocessed images
output_folder = 'features'         # Where we're gonna save the extracted features

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to extract color histogram - let's get some color magic!
def extract_color_histogram(image):
    # Calculate the histogram of the image (Hint: use cv2.calcHist)
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    return hist.flatten()

# Function to extract texture features using Local Binary Patterns (LBP)
def extract_lbp(image):
    lbp = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            center = image[i, j]
            binary_string = ''
            # Let's fill in the neighbors 
            binary_string += '1' if image[i-1, j-1] >= center else '0'
            binary_string += '1' if image[i-1, j] >= center else '0'
            binary_string += '1' if image[i-1, j+1] >= center else '0'
            binary_string += '1' if image[i, j+1] >= center else '0'
            binary_string += '1' if image[i+1, j+1] >= center else '0'
            binary_string += '1' if image[i+1, j] >= center else '0'
            binary_string += '1' if image[i+1, j-1] >= center else '0'
            binary_string += '1' if image[i, j-1] >= center else '0'
            lbp[i, j] = int(binary_string, 2)
    return lbp.flatten()

# Function to extract edges using the Canny method - let’s find those edges!
def extract_edges(image):
    # Use cv2.Canny to detect edges 
    edges = cv2.Canny(image, 100, 200)   

# Looping through all our images to extract features
for image_name in os.listdir(input_folder):
    if image_name.endswith('.png') or image_name.endswith('.jpg'):
        # Read the image in grayscale 
        image_path = os.path.join(input_folder, image_name)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  

        # Extract features
        color_hist = extract_color_histogram(image)   # Color histogram
        lbp_features = extract_lbp(image)             # Texture using LBP
        edges = extract_edges(image)                 # Edges using Canny

        # Save features to a .npy file (Numpy's way of saving stuff)
        np.save(os.path.join(output_folder, f"{image_name}_color_hist.npy"), color_hist)
        np.save(os.path.join(output_folder, f"{image_name}_lbp.npy"), lbp_features)
        np.save(os.path.join(output_folder, f"{image_name}_edges.npy"), edges)

        print(f"Features extracted and saved for: {image_name}")

print("Feature extraction completed! 🎉")
