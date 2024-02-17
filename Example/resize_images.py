import os
from PIL import Image

def resize_images(input_folder, output_folder, width=768, height=1024):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for i, filename in enumerate(os.listdir(input_folder)):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{i+1}.jpg")
            # Open, resize, and save the image
            with Image.open(input_path) as img:
                resized_img = img.resize((width, height))
                resized_img.save(output_path)

# Example usage
input_folder = "input_images"
# Change this to your input folder path
output_folder = "output_images" 
# Change this to the desired output folder path
resize_images(input_folder, output_folder)