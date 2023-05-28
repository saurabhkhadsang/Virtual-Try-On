
# Openpose_img/json -> openpose_img/json

import os
import shutil

def copy_files(source_dir, destination_dir_img, destination_dir_json):
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        base_name, ext = os.path.splitext(file_name)

        if ext == ".png":
            destination_file = os.path.join(destination_dir_img, file_name)
            if os.path.isfile(destination_file):
                # If file already exists in the destination directory, replace it
                os.remove(destination_file)
            shutil.copy2(source_file, destination_dir_img)
            print(f"Copied image file: {file_name}")
        elif ext == ".json":
            destination_file = os.path.join(destination_dir_json, file_name)
            if os.path.isfile(destination_file):
                # If file already exists in the destination directory, replace it
                os.remove(destination_file)
            shutil.copy2(source_file, destination_dir_json)
            print(f"Copied JSON file: {file_name}")

# Example usage:
source_directory = "D:\MP3_Django_Test_2_W\myproject\OpenP_W\openpose\output"
destination_directory_images = "D:\MP3_Django_Test_2_W\myproject\_Data\openpose_img"
destination_directory_json = "D:\MP3_Django_Test_2_W\myproject\_Data\openpose_json"

copy_files(source_directory, destination_directory_images, destination_directory_json)
