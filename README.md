# Image-Resizer
This Python script allows you to resize images in a specified folder and save the resized images to another folder.
Sure, here's a detailed README.md document for your GitHub repository:

---

# Image Resizer

This Python script allows you to resize images in a specified folder and save the resized images to another folder.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x (3.10 used)
- Pillow library (`pip install pillow`)

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/image-resizer.git
   ```

2. Navigate to the directory:

   ```bash
   cd image-resizer
   ```

3. Modify the `input_folder` and `output_folder` variables in the `resize_images.py` script according to your directory structure:

   ```python
   input_folder = "input_images"  # Change this to your input folder path
   output_folder = "output_images"  # Change this to the desired output folder path
   ```

4. Run the script:

   ```bash
   python resize_images.py
   ```

   This will resize all images in the `input_images` folder (or your specified input folder) to the default size of 768x1024 pixels and save them to the `output_images` folder (or your specified output folder).

5. Optionally, you can adjust the `width` and `height` parameters in the `resize_images` function call to resize images to your desired dimensions:

   ```python
   resize_images(input_folder, output_folder, width=desired_width, height=desired_height)
   ```

## Example

Suppose you have a folder named `input_images` containing images you want to resize. You want to resize them to a width of 800 pixels and a height of 600 pixels and save them to a folder named `resized_images`.

Your `resize_images.py` script should look like this:

```python
input_folder = "input_images"
output_folder = "resized_images"
resize_images(input_folder, output_folder, width=800, height=600)
```

After running the script, resized images will be saved in the `resized_images` folder.

You can check the Example folder to get the proper understanding of the script.

## Notes

- Supported image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`.
- The script will create the output folder if it doesn't exist.

---

Feel free to customize this README further based on your specific preferences or additional information you'd like to provide.
