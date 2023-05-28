
# X_Cloth_mask/output -> cloth_mask
# X_Cloth_mask/input -> cloth

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



#  X_Cloth_mask/output -> cloth-mask
source_directory = "D:\MP3_Django_Test_2_W\myproject\X_Cloth _Mask_W\cloth-seg\output_images"
destination_directory = "D:\MP3_Django_Test_2_W\myproject\_Data\cloth-mask"
copy_files(source_directory, destination_directory)


# X_Cloth_mask/input -> cloth
source_directory = "D:\MP3_Django_Test_2_W\myproject\X_Cloth _Mask_W\cloth-seg\input_images"
destination_directory = "D:\MP3_Django_Test_2_W\myproject\_Data\cloth"
copy_files(source_directory, destination_directory)