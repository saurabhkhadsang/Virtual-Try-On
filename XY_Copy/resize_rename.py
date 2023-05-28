from PIL import Image, ImageOps
import os

# List of folders containing the images
folder_paths = [
    r"D:\MP3_Django_Test_2_W\myproject\_INPUT\cloth",
    r"D:\MP3_Django_Test_2_W\myproject\_INPUT\pose"
]

# Iterate over each folder
for folder_path in folder_paths:
    # Get the path of the image files in the folder
    image_files = os.listdir(folder_path)
    if len(image_files) == 0:
        print("No image files found in the folder:", folder_path)
        continue

    # Iterate over each image file in the folder
    for image_file_name in image_files:
        image_file = os.path.join(folder_path, image_file_name)

        # Open the image using Pillow
        image = Image.open(image_file)

        # Convert the image to RGB mode
        image = image.convert("RGB")

        # Resize the image with padding
        new_size = (768, 1024)
        resized_image = ImageOps.pad(image, new_size)

        # Rename the image to "0.jpg"
        new_image_file = os.path.join(folder_path, "0.jpg")

        # Save the resized image as JPEG
        resized_image.save(new_image_file, "JPEG")

        # Delete the original image file
        os.remove(image_file)

        print("Image resized, renamed, and original file deleted successfully:", image_file)

print("All images resized, renamed, and original files deleted successfully.")
