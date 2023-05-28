
# image -> image
# image-parse-v3 -> image-parse-v3
# openpose_json -> openpose_json

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



# image -> image
source_directory = r"D:\MP3_Django_Test_2_W\myproject\_Data\image"
destination_directory = r"D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W\test\image"
copy_files(source_directory, destination_directory)

# image-parse-v3 -> image-parse-v3
source_directory = r"D:\MP3_Django_Test_2_W\myproject\_Data\image-parse-v3"
destination_directory = r"D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W\test\image-parse-v3"
copy_files(source_directory, destination_directory)


# openpose_json -> openpose_json
source_directory = r"D:\MP3_Django_Test_2_W\myproject\_Data\openpose_json"
destination_directory = r"D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W\test\openpose_json"
copy_files(source_directory, destination_directory)

