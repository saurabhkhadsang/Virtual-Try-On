
# cloth -> X_Cloth_Mask_W

import os
import shutil

def copy_files(source_dir, destination_dir):
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        if os.path.isfile(destination_file):
            # If file already exists in the destination directory, replace it
            os.remove(destination_file)

        shutil.copy2(source_file, destination_dir)
        print(f"Copied: {file_name}")

# Example usage:
source_directory = "D:\MP3_Django_Test_2_W\myproject\_INPUT\cloth"
destination_directory = "D:\MP3_Django_Test_2_W\myproject\X_Cloth _Mask_W\cloth-seg\input_images"

copy_files(source_directory, destination_directory)
