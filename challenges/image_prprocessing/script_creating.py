import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load the medical image
image_path = 'challenges/image_prprocessing/input_images/patch_4096_11776.png'
image = cv2.imread(image_path)

# Convert the image to a PIL format for text manipulation
image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert OpenCV image to PIL format

# Create a function to add styled text
def add_text_to_image(image_pil, text, position, font_path, font_size, color, alignment):
    # Create a drawing context
    draw = ImageDraw.Draw(image_pil)
    
    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()
    
    # Add text with specified attributes
    draw.text(position, text, fill=color, font=font, align=alignment)

    return image_pil

# Call the function to add text to your image
modified_image = add_text_to_image(
    image_pil=image_pil, 
    text="Tumor Detected", 
    position=(50, 50), 
    font_path="arial.ttf",  # Replace with your specific font path
    font_size=40, 
    color=(255, 0, 0),  # Red color for text
    alignment="left"
)

# Convert the modified PIL image back to OpenCV format (NumPy array)
modified_image_cv = np.array(modified_image)  # Convert PIL image to NumPy array

# Make sure to convert the image to uint8 type
modified_image_cv = modified_image_cv.astype(np.uint8)

# Convert from RGB (used by PIL) to BGR (used by OpenCV)
modified_image_cv = cv2.cvtColor(modified_image_cv, cv2.COLOR_RGB2BGR)

# Save the modified image
output_path = 'challenges/image_prprocessing/output/annotated_image.png'
cv2.imwrite(output_path, modified_image_cv)

# Display the image
cv2.imshow('Annotated Image', modified_image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
