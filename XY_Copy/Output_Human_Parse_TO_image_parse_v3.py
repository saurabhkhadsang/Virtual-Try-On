
# Human_Parse_W/output -> image-parse-v3
# Human_Parse_W/input -> image


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


# Human_Parse_W/output -> image-parse-v3
source_directory = "D:\MP3_Django_Test_2_W\myproject\Human_Parse_W\image_segmentation\human_part_segmentation\output"
destination_directory = "D:\MP3_Django_Test_2_W\myproject\_Data\image-parse-v3"
copy_files(source_directory, destination_directory)


# Human_Parse_W/input -> image
source_directory = "D:\MP3_Django_Test_2_W\myproject\Human_Parse_W\image_segmentation\human_part_segmentation\input"
destination_directory = "D:\MP3_Django_Test_2_W\myproject\_Data\image"
copy_files(source_directory, destination_directory)
